# Setup 

1. Update `infra/template.yaml` by adding/updating: 

    a. AppSyncApiKey
    b. API
    c. Schema
    d. Dynamo DB table
    e. Data source 
    f. Resolvers

    and define your graphql schema inside `infra/src/schema.graphql`

2. Build the app:

    ```console
    sam build
    sam deploy --profile <profile> --stack-name 
    ```

3. update the queries in 

    This command will use the configuration already provided inside the `infra/src/schema.graphql` file.

# Guide 

* *Resolver*: a resolver is a unit of code that handles how that field's data will be resolved when a request is made to the service. They are most commonly used to implement the state-changing operations for your query, mutation, and subscription field operations. In this case they contains the logic to speak with DynamoDB Table. See [Resolvers](https://docs.aws.amazon.com/appsync/latest/devguide/resolver-components.html).

* *Data Source*: The schema is like a gateway that handles all requests made to the server. When a request is made, the schema acts as the single endpoint that interfaces with the client. The schema will access, process, and relay data from the data source back to the client. See [Data Source](https://docs.aws.amazon.com/appsync/latest/devguide/data-source-components.html).

# References

[Deploy AppSync GraphQL API with SAM](https://medium.com/aws-serverless-world/deploy-appsync-graphql-api-with-sam-part-one-18287b55951b)