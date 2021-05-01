extern crate pretty_env_logger;
use hyper::service::{make_service_fn, service_fn};
use hyper::{Body, Method, Request, Response, Server};
use rayon::prelude::*;
use std::convert::Infallible;
use std::path::Path;

enum Mode {
    EncodeEverything,
    EncodeOnlyBinaries,
    SkipNonUtf8Files,
}

const ROOT: &str = "."; // TODO: pass it as a CLI args
const MODE: Mode = Mode::SkipNonUtf8Files; // ...

#[derive(serde::Serialize)]
struct SystemTime {}

#[derive(serde::Serialize)]
struct FileType {}

#[derive(serde::Serialize)]
struct Permissions {}

#[derive(serde::Serialize)]
struct Metadata {
    file_type: FileType,
    is_dir: bool,
    is_file: bool,
    permissions: Permissions,
    modified: SystemTime,
    accessed: SystemTime,
    created: SystemTime,
}

#[derive(serde::Serialize)]
enum Content {
    Base64(String),
    Utf8(String),
    Skiped,
    Folder,
}

#[derive(serde::Serialize)]
struct Entry {
    // metadata: Metadata, // TODO
    path: String,
    content: Content,
}

fn utf8(path: &Path) -> Result<Content, ()> {
    match std::fs::read_to_string(path) {
        Ok(x) => Ok(Content::Utf8(x)),
        Err(_) => Err(()),
    }
}

fn base64(path: &Path) -> Content {
    Content::Base64(base64::encode(
        std::fs::read(path).expect("Failed to read file"),
    ))
}

fn entry(path: &Path) -> Entry {
    // TODO: log path
    let metadata = path.metadata().expect("Failed to read metadata");
    Entry {
        path: path.display().to_string(),
        content: if metadata.is_file() {
            match MODE {
                Mode::EncodeEverything => base64(path),
                Mode::EncodeOnlyBinaries => utf8(path).unwrap_or_else(|_| base64(path)),
                Mode::SkipNonUtf8Files => utf8(path).unwrap_or(Content::Skiped),
            }
        } else {
            Content::Folder
        },
    }
}

fn jtar(dir: &str) -> String {
    let mut paths = vec![];
    for entry in glob::glob(dir).expect("Failed to read glob pattern") {
        paths.push(entry.unwrap());
    }
    let entries: Vec<Entry> = paths.par_iter().map(|x| entry(x)).collect();
    serde_json::to_string(&entries).expect("Failed to encode JSON")
}

fn jsh(_path: &str, cmd: &str) -> String {
    String::from(cmd) // /!\ FIX ME /!\
}

async fn handle(request: Request<Body>) -> Result<Response<Body>, Infallible> {
    let response = match *request.method() {
        Method::GET => jtar(&format!("{}{}", ROOT, &request.uri())),
        Method::POST => jsh(
            &format!("{}{}", ROOT, &request.uri()),
            &format!("{:?}", &request.body()),
        ),
        _ => format!("Method {} not handled", request.method()), // TODO: JSON
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
