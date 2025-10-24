# AWS S3 Vectors - Document Storage & Search Implementation

## Overview

This implementation demonstrates AWS S3 Vectors functionality for cost-optimized vector storage and semantic document search. S3 Vectors reduces vector storage costs by up to 90% compared to traditional vector databases.

## 🚀 Features Implemented

- **Vector Storage**: Purpose-built storage for document embeddings
- **Semantic Search**: Find documents by meaning, not just keywords
- **Metadata Filtering**: Rich filtering by document attributes
- **Cost Optimization**: Up to 90% cost reduction vs traditional vector DBs
- **Sub-second Queries**: Fast similarity search performance

## 📁 Files Structure

```
├── s3-vectors.html              # Web documentation page
├── document_vector_storage.py   # Main storage implementation
├── query_document_vectors.py    # Search and query functionality
├── requirements.txt             # Python dependencies
└── S3_VECTORS_README.md        # This documentation
```

## 🔧 Implementation Details

### Sample Documents Stored
- `annual_report_2024.pdf` - Financial report (finance department)
- `product_manual.docx` - Product documentation (product team)
- `meeting_notes.pdf` - Executive meeting notes (executive team)

### Vector Specifications
- **Dimensions**: 384 (compatible with most embedding models)
- **Storage Format**: JSON with metadata
- **Similarity Metric**: Cosine similarity
- **Metadata Schema**: Document type, department, author, year, creation date

### S3 Storage Structure
```
s3://my-vector-documents-bucket/
├── vectors/
│   ├── index_metadata.json
│   └── documents/
│       ├── 37c2225a85cfbde4f936b6b84c9936c7.json
│       ├── 4ab3f81e274d2396d88a892783ae116e.json
│       └── 47883cde719a0e3a05a532a279ef98e5.json
```

## 🏃‍♂️ Quick Start

### Prerequisites
```bash
pip install boto3 numpy
```

### 1. Store Document Embeddings
```bash
python document_vector_storage.py
```

### 2. Query Documents
```bash
python query_document_vectors.py
```

## 🔍 Query Examples

### Semantic Search
```python
results = query_engine.search_similar_documents("financial report revenue", top_k=3)
```

### Metadata Filtering
```python
finance_docs = query_engine.filter_by_metadata({"document_type": "financial_report"})
product_docs = query_engine.filter_by_metadata({"department": "product"})
```

## 🎯 Use Cases

- **Medical Imaging**: Find similarities across millions of medical images
- **Copyright Detection**: Identify derivative content in media libraries
- **Enterprise Search**: Semantic search across corporate documents
- **Video Understanding**: Search for specific scenes within video content
- **Personalization**: Deliver tailored recommendations
- **Image Deduplication**: Remove duplicate images from collections

## 🔗 AWS Service Integrations

### Amazon OpenSearch Service
- Export to OpenSearch Serverless for high-performance search
- Use S3 Vectors as cost-effective storage engine

### Amazon Bedrock
- Native integration with Bedrock Knowledge Bases
- Support for RAG (Retrieval Augmented Generation) applications

## 🚀 Production Deployment

When S3 Vectors becomes fully available:

```bash
# Create vector bucket
aws s3vectors create-vector-bucket --bucket-name my-vectors

# Create vector index  
aws s3vectors create-vector-index --bucket-name my-vectors --index-name documents

# Upload vectors
aws s3vectors put-vectors --bucket-name my-vectors --index-name documents

# Query vectors
aws s3vectors query-vectors --bucket-name my-vectors --index-name documents --query-vector [...]
```

## 📊 Performance Metrics

- **Query Latency**: Sub-second response times
- **Recall Rate**: 90%+ average recall for most datasets
- **Cost Savings**: Up to 90% reduction in storage and query costs
- **Scalability**: Store billions of vectors with S3-level durability

## 🔒 Security Features

- IAM policies and Service Control Policies support
- Dedicated `s3vectors` namespace for granular permissions
- Block Public Access always enabled (cannot be disabled)
- Encryption at rest and in transit

## 🌐 Web Interface

Visit the [S3 Vectors Demo Page](./s3-vectors.html) for a comprehensive web-based documentation with:
- Interactive feature overview
- Implementation details
- Code examples
- Integration guides

## 📈 Migration Path

The current implementation structure is fully compatible with S3 Vectors format, enabling seamless migration when the service becomes available in your region.

## 🤝 Contributing

This implementation is part of the AWS Week 2.0 project. Feel free to extend and improve the functionality.

## 📄 License

This project is part of the AWS learning initiative and follows standard AWS documentation practices.
