//! # Pandoro
//!
//! _HTTP API of filesystem_
//!
//! Pandoro let you `GET` a [jtar](https://github.com/cppccn/jtar) archive of a
//! given URL path and `POST` a [jsh](https://github.com/cppccn/jsh) of
//! transactionnal commands.
//!
//! ## Core concept
//!
//! The aims and purpose of Pandoro is to use filesystems abstractions are a
//! common intermediate representation that allows developers to rapidly
//! prototype and to easily switch between different database engines: FUSE
//! drivers allow to mount a everything as a drive (e.g.
//! [PostgreSQL](https://github.com/petere/postgresqlfs),
//! [SSH](https://github.com/libfuse/sshfs),
//! [WebDAV](https://wiki.archlinux.org/index.php/Davfs2), etc.)
//!
//! In the future, we want to offer a complete CRUD REST API and support of
//! GraphQL format would a nice bonus.

extern crate jshell;
extern crate jtar;
extern crate pretty_env_logger;
use hyper::service::{make_service_fn, service_fn};
use hyper::{Body, Method, Request, Response, Server};
use std::convert::Infallible;
use std::path::Path;

const ROOT: &str = "."; // TODO: pass it as a CLI args

async fn handle(request: Request<Body>) -> Result<Response<Body>, Infallible> {
    let dir = Path::new(ROOT).join(&request.uri().path());
    let response = match *request.method() {
        Method::GET => jtar::compress(&dir),
        Method::POST => jshell::exec(&dir, &format!("{:?}", &request.body())),
        _ => format!("Method {} not handled", request.method()), // FIXME
    };
    Ok(Response::new(Body::from(response)))
}

async fn shutdown_signal() {
    // Wait for the CTRL+C signal
    tokio::signal::ctrl_c()
        .await
        .expect("failed to install CTRL+C signal handler");
}

#[tokio::main]
pub async fn main() -> Result<(), Box<dyn std::error::Error + Send + Sync>> {
    pretty_env_logger::init();

    // For every connection, we must make a `Service` to handle all
    // incoming HTTP requests on said connection.
    let make_svc = make_service_fn(|_conn| {
        // This is the `Service` that will handle the connection.
        // `service_fn` is a helper to convert a function that
        // returns a Response into a `Service`.
        async { Ok::<_, Infallible>(service_fn(handle)) }
    });

    // Constructed `addr` and `make_svc` from your app above..
    let addr = ([127, 0, 0, 1], 3000).into();

    // And construct the `Server` like normal...
    let server = Server::bind(&addr).serve(make_svc);

    println!("Listening on http://{}", addr);

    // And now add a graceful shutdown signal...
    let graceful = server.with_graceful_shutdown(shutdown_signal());

    // Run this server for... forever!
    if let Err(e) = graceful.await {
        eprintln!("Server error: {}", e);
    }

    Ok(())
}
