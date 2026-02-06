FROM public.ecr.aws/lambda/python:3.12

# Install cwebp for WebP conversion
RUN dnf install -y libwebp-tools && dnf clean all

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy handler code
COPY app.py .

CMD ["app.compressor_handler"]
