# Lab 03 - Build your module

## Objective

- _Daggerize_ an existing application.
- Build a Docker image.
- Publish a Docker image to a remote registry.
- Serve the app directly from Dagger.

## Prerequisites

- [Install Dagger](https://docs.dagger.io/install)
- [Clone this repository](https://github.com/0xbochi/daggerxbochi)

```shell
git clone https://github.com/0xbochi/daggerxbochi
cd lab03
```

## Build your module

 1. Initializes a new Python module.

```shell
dagger init --sdk python --name daggerxbochie --source .
```

 2. Setup IDE integration.

To do so, refer to the [official Dagger documentation](https://docs.dagger.io/manuals/developer/ide-integration).

 3. Create a function to build from the existing Dockerfile

```python
@function
def build_from_dockerfile(
    self,
    source: Directory,
) -> Container:
    return source.docker_build()
```

```shell
dagger call build-from-dockerfile --source .
```

 4. Create a function to publish the image to a remote registry

```python
@function
def publish(
    self,
    source: Directory
) -> str:
    return self.build_from_dockerfile(source).publish(
        address="ttl.sh/daggerxbochi:2h"
    )
```

```shell
dagger call publish --source .

docker run -p 5001:5001 ttl.sh/daggerxbochi:2h@<your sha>
```

 5. Create a function to serve the app directly from Dagger

```python
@function
def serve(
    self,
    source: Directory,
    port: int = 5001,
) -> Service:
    return (
        self.build(source)
            .with_exposed_port(port)
            .with_exec(["python", "app.py"])
            .as_service()
    )
```

```shell
dagger call serve --source . --port 5001 up
```

 6. Build the image with Dagger instructions

```python
@function
def build(
    self,
    source: Directory,
) -> Container:
    return (
        dag.container()
        .from_("python:3.9-slim")
        .with_directory("/app", source)
        .with_workdir("/app")
        .with_exec(["pip", "install", "flask"])
        .with_entrypoint(["python", "app.py"])
    )
```

```shell
dagger call build --source .
```

For debug purposes, you can also directly open a shell in the container

```shell
dagger call build --source . terminal --cmd /bin/sh
```

 7. Replace the function `build_from_dockerfile` with `build`

Your CI is now fully _daggerized_ 🚀

## Conclusion

We learn how to build a module with Dagger and several useful features to help us develop locally.

Thanks for following these labs 🙏