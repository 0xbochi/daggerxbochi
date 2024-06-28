# Lab 01 - Introduction to Dagger

## Objective

- Understand Dagger fundamentals.
- Learn how to use the DaggerCLI.
- Learn what's a Dagger module.
- Run your first dagger command.
- Discover the Dagger API & SDK.

## Prerequisites

- [Install Dagger](https://docs.dagger.io/install)

## A. First steps with Dagger

 1. Verify you have dagger installed on your host.

```shell
dagger version
# dagger v0.11.8 (registry.dagger.io/engine) darwin/arm64
```
 
 2. Discover the Dagger CLI

```shell
dagger --help
```

 3. Init a module with your favorite language

```shell
dagger init --sdk go --name quickstart
```

 4. List the function available in the module

```shell
dagger functions
```

 5. Run the quickstart function

This builds a simple `alpine` container, runs echo `hello` bochi` and returns the `stdout` as a result of the function.

```shell
dagger call container-echo --string-arg "hello bochi" stdout
```

## B. Extends your module features with external modules from the [Daggerverse](https://daggerverse.dev/)

🔥 We recently added the multi-VCS support for Dagger, see our progress on: https://github.com/dagger/dagger/pull/7511, it should be
added to the next release (`v0.12.0`).

 1. List functions of an external module

```shell
dagger -m github.com/vito/daggerverse/go@v0.0.1 functions
```

 2. Check the specific inputs of a function

```shell
dagger -m github.com/vito/daggerverse/go@v0.0.1 call base --help
``` 

 3. Open a runtime shell inside the base container of the external module

```shell
dagger -m github.com/vito/daggerverse/go@v0.0.1 call base terminal
```


## Conclusion

That's it for the first lab, you explored the basics of Dagger and learned how to use the Dagger CLI.

Now it's time to explore some real use cases & implementation, go to [lab02](../lab02/README.md) to continue.