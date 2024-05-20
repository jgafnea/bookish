FROM python:3.12-slim AS base

# If needing to add packages, do it here.
# Install/update pip and system packages
# RUN pip install --upgrade pip
# RUN apt update && apt -y upgrade && \
# 	rm -rf /var/lib/apt/lists/*

FROM base AS builder

WORKDIR /build
COPY . ./
ENV PATH  $PATH:/root/.local/bin

# Install poetry using pipx, not pip, per poetry docs
RUN pip install pipx && pipx install poetry && \
	poetry build && pip install dist/*.whl

FROM base AS runner 
COPY --from=builder /usr/local /usr/local

WORKDIR /app
ENTRYPOINT ["bookish"]
