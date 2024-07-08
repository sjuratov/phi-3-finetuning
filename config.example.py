# Azure settings
AZURE_SUBSCRIPTION_ID = "<Azure ML WS Subscription ID>"
AZURE_RESOURCE_GROUP_NAME = "<Azure ML WS RG>" # "TestGroup"

# Azure Machine Learning settings
AZURE_ML_WORKSPACE_NAME = "<Azure ML WS Name>" # "finetunephi-workspace"

# Azure Managed Identity settings
AZURE_MANAGED_IDENTITY_CLIENT_ID = "<Azure MID Client ID>"
AZURE_MANAGED_IDENTITY_NAME = "<Azure MID Name>" # "finetunephi-mangedidentity"
AZURE_MANAGED_IDENTITY_RESOURCE_ID = f"/subscriptions/{AZURE_SUBSCRIPTION_ID}/resourceGroups/{AZURE_RESOURCE_GROUP_NAME}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{AZURE_MANAGED_IDENTITY_NAME}"

# Dataset file paths
TRAIN_DATA_PATH = "data/train_data.jsonl"
TEST_DATA_PATH = "data/test_data.jsonl"

# Fine-tuned model settings
AZURE_MODEL_NAME = "finetune-phi-model" # "finetune-phi-model"
AZURE_ENDPOINT_NAME = "finetune-phi-endpoint" # "finetune-phi-endpoint"
AZURE_DEPLOYMENT_NAME = "finetune-phi-deployment" # "finetune-phi-deployment"

AZURE_ML_API_KEY = "<Azure ML Online Managed Endpoint Key>"
AZURE_ML_ENDPOINT = "<Azure ML Online Managed Endpoint>" # "https://{your-endpoint-name}.{your-region}.inference.ml.azure.com/score"