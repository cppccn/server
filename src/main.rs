extern crate pretty_env_logger;

use glob::glob;

use std::convert::Infallible;

use hyper::service::{make_service_fn, service_fn};
use hyper::{Body, Request, Response, Server};

fn search(path: &str) -> Vec<String> {
    let mut paths = vec![];
    for entry in glob(path).expect("Failed to read glob pattern") {
        paths.push(match entry {
            Ok(path) => format!("{}", path.display()),
            Err(e) => panic!("{}", e),
        });
    }
    paths
}

async fn handle(request: Request<Body>) -> Result<Response<Body>, Infallible> {
    let root = "."; // TODO: pass it as a CLI args...
    let results = search(&format!("{}{}", root, &request.uri()));
    let response = format!("{:?}", results); // FIXME: serde_json::from_vec()
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