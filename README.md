# Django to Azure Appservice stack

[![Use this template](https://github.com/stack-instance/badge.svg)](https://github.com/stack-instance?stack_template_owner=harshiniks&stack_template_repo=django-to-azure-appservice-stack)                     

 <p>
    <img src="https://avatars.githubusercontent.com/u/6844498?s=200&v=4" height="20">
    <b>Use this stack</b> to spin up a django app and deploy to azure in seconds.
</p>


## Why should you use this stack?
You can spin up your own Django website in seconds...

Deployment happens on Azure Cloud via a Azure App Service.

The stack also sets up a proper Github CI/CD environment by taing care of the following things
1. Branch Naming convention - You can use any branch prefixed with "dev" as your development environment. 
2. Branch Protection Setting - Developers working on this branch can work freely and push changes without a PR and a code reviewer. This facilitates quick development.

Note: Once you create a repo out of this stack, you can find your website deployed at <azure_app_name>.azurewebsites.net.

## What are the inputs to pass while setting up the stack?
```
# Name of the Azure App which has been configured to host the website
- AZURE_APP_NAME

# Azure Credentials, this can be obtained using Azure cli
- AZURE_CREDENTIALS
```
The value of AZURE_CREDENTIALS is expected to be a JSON object that represents a service principal (an identifer for an application or process) that authenticates the workflow with Azure.

To function correctly, this service principal must be assigned the [Contributor]((https://docs.microsoft.com/azure/role-based-access-control/built-in-roles#contributor)) role for the web app or the resource group that contains the web app.

The following steps describe how to create the service principal, assign the role, and create a secret in your repository with the resulting credentials.

1. Open the Azure Cloud Shell at [https://shell.azure.com](https://shell.azure.com). You can alternately use the [Azure CLI](https://docs.microsoft.com/cli/azure/install-azure-cli?view=azure-cli-latest) if you've installed it locally. (For more information on Cloud Shell, see the [Cloud Shell Overview](https://docs.microsoft.com/azure/cloud-shell/overview).)
  
2. Use the [az ad sp create-for-rbac](https://docs.microsoft.com/cli/azure/ad/sp?view=azure-cli-latest#az_ad_sp_create_for_rbac) command to create a service principal and assign a Contributor role:

    ```azurecli
    az ad sp create-for-rbac --name "{sp-name}" --sdk-auth --role contributor \
        --scopes /subscriptions/{subscription-id}/resourceGroups/{resource-group}/providers/Microsoft.Web/sites/{app-name}
    ```

    Replace the following:
      * `{sp-name}` with a suitable name for your service principal, such as the name of the app itself. The name must be unique within your organization.
      * `{subscription-id}` with the subscription you want to use
      * `{resource-group}` the resource group containing the web app.
      * `{app-name}` with the name of the web app.

    This command invokes Azure Active Directory (via the `ad` part of the command) to create a service principal (via `sp`) specifically for [Role-Based Access Control (RBAC)](https://docs.microsoft.com/azure/role-based-access-control/overview) (via `create-for-rbac`).

    The `--role` argument specifies the permissions to grant to the service principal at the specified `--scope`. In this case, you grant the built-in [Contributor](https://docs.microsoft.com/azure/role-based-access-control/built-in-roles#contributor) role at the scope of the web app in the specified resource group in the specified subscription.

    If desired, you can omit the part of the scope starting with `/providers/...` to grant the service principal the Contributor role for the entire resource group:

    ```azurecli  
    az ad sp create-for-rbac --name "{sp-name}" --sdk-auth --role contributor \
        --scopes /subscriptions/{subscription-id}/resourceGroups/{resource-group}
    ```

    For security purposes, however, it's always preferable to grant permissions at the most restrictive scope possible.

3. When complete, the `az ad sp create-for-rbac` command displays JSON output in the following form (which is specified by the `--sdk-auth` argument):

    ```json
    {
      "clientId": "<GUID>",
      "clientSecret": "<GUID>",
      "subscriptionId": "<GUID>",
      "tenantId": "<GUID>",
      (...)
    }
    ```

#### Github apps installed with this stack
```None```

## How to setup local development server?
```
Pre-requisites:
- Python3
- Django

Run following commands to install dependencies and view the app in the browser:
- sudo pip install -r requirements.txt
- python3 manage.py migrate
- python3 manage.py runserver
- open http://127.0.0.1:8000/
```

## Learn more 

### Django
Visit [Djangoproject.com](https://www.djangoproject.com/) to view the full documentation.

### Azure Cloud
Learn more about [Azure](https://docs.microsoft.com/en-us/azure) from the official site.


## Other Useful links

#### Security guide
Please see our guide lines for reporting issues related to [security.md](/.github/stacks/security.md).

#### Contributor guide
Please see our guide lines for [contributing.md](/.github/stacks/contributing.md).

## Contributors 
- Harshini K S ([@harshiniks](harshiniks@github.com))
