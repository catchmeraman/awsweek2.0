# Sample Documents for S3 Vectors Demo

This directory contains sample documents used in the S3 Vectors semantic search demonstration.

## Documents

### 1. Annual Report 2024 (`annual_report_2024.md`)
- **Type**: Financial Report
- **Department**: Finance Team
- **Content**: Company financial performance, achievements, and future outlook
- **Use Case**: Business intelligence and financial analysis queries

### 2. Product Manual (`product_manual.md`)
- **Type**: Technical Documentation
- **Department**: Engineering Team  
- **Content**: CloudSync Pro installation, configuration, and troubleshooting guide
- **Use Case**: Technical support and product documentation searches

### 3. Meeting Notes (`meeting_notes.md`)
- **Type**: Operational Documentation
- **Department**: Operations Team
- **Content**: Infrastructure monitoring, security compliance, and capacity planning discussions
- **Use Case**: Operational insights and process documentation queries

## Vector Embeddings

These documents have been converted to 384-dimensional vector embeddings and stored in:
- **S3 Vector Bucket**: `s3vector`
- **Vector Index**: `documents`
- **Region**: `us-east-1`

## Metadata Schema

Each document includes the following metadata:
```json
{
  "document_name": "filename.extension",
  "document_type": "report|manual|notes",
  "department": "finance|engineering|operations",
  "author": "Team Name",
  "year": "2024"
}
```

## Usage

These documents demonstrate semantic search capabilities where users can:
- Search for financial information across reports
- Find technical solutions in product manuals
- Discover operational insights from meeting notes
- Query across document types for comprehensive results

## Integration

The documents are integrated with:
- S3 Vectors native service for vector storage
- Semantic search functionality via cosine similarity
- Interactive demo page at https://dfitqm3lm3maf.amplifyapp.com
- Python scripts for vector operations and querying
