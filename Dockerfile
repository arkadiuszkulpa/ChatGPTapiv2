FROM public.ecr.aws/lambda/python:3.9-rapid-x86_64

# Copy requirements.txt file
COPY requirements.txt ${LAMBDA_TASK_ROOT}
#Install the specified packages
RUN pip install -r requirements.txt 

# Copy all files in source directory to the lambda task root
COPY ChatGPTapiv2-HelloWorldFunction-rBYo9f3fV7bq/* ${LAMBDA_TASK_ROOT}

# Set the CMD to your handler (could also be done as a parameter override outside of the Dockerfile)
CMD ["app.lambda_handler"]

