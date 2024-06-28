import dagger

from dagger import dag, function, object_type, Directory, Container, Service

@object_type
class Daggerxbochi:
    @function
    def build_from_dockerfile(
        self,
        source: Directory,
    ) -> Container:
        return source.docker_build()
    
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

    @function
    def publish(
        self,
        source: Directory
    ) -> str:
        return self.build(source).publish(
            address="ttl.sh/daggerxbochi:2h"
        )
