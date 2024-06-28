# Lab 02 - A real use case for Dagger

## Objective

- Discover a basic multi-source CI implementation with Dagger.
- Enjoy the benefits of Dagger.
- Learn more Dagger features.
- Run more complex workflows using the Dagger CLI.

## Prerequisites

- [Install Dagger](https://docs.dagger.io/install)
- [Clone the Greeting API repo](https://github.com/kpenfound/greetings-api.git)

```shell
git clone https://github.com/kpenfound/greetings-api.git
```

## Steps

 1. List functions in the module

```shell
dagger functions
```

 2. Take time to explore the source code in [`ci/`](https://github.com/kpenfound/greetings-api/tree/main/DEMO.md) and check the [`DEMO.md`](https://github.com/kpenfound/greetings-api/tree/main/DEMO.md) file

 3. Serve the application locally

```shell
dagger call serve --source . up 
```

 4. Run the test pipeline

```shell
dagger call test --source .
```

 5. Run the lint pipeline

```shell
dagger call lint --source .
```

 6. Run the build pipeline

```shell
dagger call build --source . -o ./build
```

 7. Run the full pipeline

```shell
dagger call all --source .
```

## Conclusion

Now that we discovered a more complex use case for Dagger, we're ready to develop our own Dagger module.

Go to [lab03](../lab03/README.md) to continue.