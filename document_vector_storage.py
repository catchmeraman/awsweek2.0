#!/usr/bin/env python3
"""
Document Vector Storage for S3 Vectors
Creates embeddings from PDF/Word documents and stores them in S3 vector format
"""

import boto3
import json
import numpy as np
from typing import List, Dict, Any
import hashlib
from datetime import datetime

class DocumentVectorStorage:
    def __init__(self, bucket_name: str, region: str = 'us-east-1'):
        self.bucket_name = bucket_name
        self.region = region
        self.s3_client = boto3.client('s3', region_name=region)
        
    def create_sample_embeddings(self) -> List[Dict[str, Any]]:
        """Create sample document embeddings for demonstration"""
        documents = [
            {
                "filename": "annual_report_2024.pdf",
                "content": "Annual financial report showing 15% revenue growth",
                "metadata": {
                    "document_type": "financial_report",
                    "year": 2024,
                    "department": "finance",
                    "author": "CFO Office",
                    "created_date": "2024-01-15"
                }
            },
            {
                "filename": "product_manual.docx", 
                "content": "User manual for new product features and installation guide",
                "metadata": {
                    "document_type": "manual",
                    "year": 2024,
                    "department": "product",
                    "author": "Product Team",
                    "created_date": "2024-03-20"
                }
            },
            {
                "filename": "meeting_notes.pdf",
                "content": "Quarterly business review meeting notes and action items",
                "metadata": {
                    "document_type": "meeting_notes",
                    "year": 2024,
                    "department": "executive",
                    "author": "Executive Assistant",
                    "created_date": "2024-06-10"
                }
            }
        ]
        
        embeddings = []
        for doc in documents:
            # Simulate embedding generation (normally you'd use a model like Titan or Bedrock)
            embedding_vector = np.random.rand(384).tolist()  # 384-dimensional vector
            
            doc_id = hashlib.md5(doc["filename"].encode()).hexdigest()
            
            embeddings.append({
                "vector_id": doc_id,
                "filename": doc["filename"],
                "embedding": embedding_vector,
                "metadata": doc["metadata"],
                "content_preview": doc["content"][:100] + "..." if len(doc["content"]) > 100 else doc["content"]
            })
            
        return embeddings
    
    def store_embeddings_s3(self, embeddings: List[Dict[str, Any]]):
        """Store embeddings in S3 (simulating S3 Vectors structure)"""
        for embedding in embeddings:
            key = f"vectors/documents/{embedding['vector_id']}.json"
            
            # Structure data for S3 Vectors compatibility
            vector_data = {
                "vector_id": embedding["vector_id"],
                "embedding": embedding["embedding"],
                "metadata": {
                    "filename": embedding["filename"],
                    "content_preview": embedding["content_preview"],
                    **embedding["metadata"]
                },
                "timestamp": datetime.utcnow().isoformat(),
                "dimension": len(embedding["embedding"])
            }
            
            try:
                self.s3_client.put_object(
                    Bucket=self.bucket_name,
                    Key=key,
                    Body=json.dumps(vector_data, indent=2),
                    ContentType='application/json'
                )
                print(f"✓ Stored embedding for {embedding['filename']}")
            except Exception as e:
                print(f"✗ Error storing {embedding['filename']}: {e}")
    
    def create_vector_index_metadata(self, embeddings: List[Dict[str, Any]]):
        """Create index metadata for the vector collection"""
        index_metadata = {
            "index_name": "document_embeddings",
            "description": "Document embeddings for PDF and Word files",
            "dimension": 384,
            "total_vectors": len(embeddings),
            "created_at": datetime.utcnow().isoformat(),
            "metadata_schema": {
                "filename": "string",
                "document_type": "string", 
                "year": "number",
                "department": "string",
                "author": "string",
                "created_date": "string"
            },
            "vector_ids": [emb["vector_id"] for emb in embeddings]
        }
        
        try:
            self.s3_client.put_object(
                Bucket=self.bucket_name,
                Key="vectors/index_metadata.json",
                Body=json.dumps(index_metadata, indent=2),
                ContentType='application/json'
            )
            print("✓ Created vector index metadata")
        except Exception as e:
            print(f"✗ Error creating index metadata: {e}")

def main():
    # Configuration
    BUCKET_NAME = "my-vector-documents-bucket"
    REGION = "us-west-2"
    
    print("🚀 Setting up Document Vector Storage...")
    
    # Initialize storage
    storage = DocumentVectorStorage(BUCKET_NAME, REGION)
    
    # Create sample embeddings
    print("\n📄 Creating sample document embeddings...")
    embeddings = storage.create_sample_embeddings()
    
    print(f"Generated {len(embeddings)} document embeddings:")
    for emb in embeddings:
        print(f"  - {emb['filename']} ({emb['metadata']['document_type']})")
    
    # Store in S3
    print(f"\n☁️  Storing embeddings in S3 bucket: {BUCKET_NAME}")
    storage.store_embeddings_s3(embeddings)
    
    # Create index metadata
    print("\n📊 Creating vector index metadata...")
    storage.create_vector_index_metadata(embeddings)
    
    print(f"\n✅ Complete! Vector storage created in s3://{BUCKET_NAME}/vectors/")
    print("\nNext steps for S3 Vectors (when available):")
    print("1. Create vector bucket: aws s3vectors create-vector-bucket")
    print("2. Create vector index: aws s3vectors create-vector-index") 
    print("3. Upload vectors: aws s3vectors put-vectors")
    print("4. Query vectors: aws s3vectors query-vectors")

if __name__ == "__main__":
    main()
