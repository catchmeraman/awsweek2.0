#!/usr/bin/env python3
"""
Document Vector Query Script
Demonstrates how to query document embeddings stored in S3
"""

import boto3
import json
import numpy as np
from typing import List, Dict, Any, Tuple
import math

class DocumentVectorQuery:
    def __init__(self, bucket_name: str, region: str = 'us-west-2'):
        self.bucket_name = bucket_name
        self.region = region
        self.s3_client = boto3.client('s3', region_name=region)
        
    def load_index_metadata(self) -> Dict[str, Any]:
        """Load the vector index metadata"""
        try:
            response = self.s3_client.get_object(
                Bucket=self.bucket_name,
                Key='vectors/index_metadata.json'
            )
            return json.loads(response['Body'].read())
        except Exception as e:
            print(f"Error loading index metadata: {e}")
            return {}
    
    def load_vector(self, vector_id: str) -> Dict[str, Any]:
        """Load a specific vector by ID"""
        try:
            response = self.s3_client.get_object(
                Bucket=self.bucket_name,
                Key=f'vectors/documents/{vector_id}.json'
            )
            return json.loads(response['Body'].read())
        except Exception as e:
            print(f"Error loading vector {vector_id}: {e}")
            return {}
    
    def cosine_similarity(self, vec1: List[float], vec2: List[float]) -> float:
        """Calculate cosine similarity between two vectors"""
        dot_product = sum(a * b for a, b in zip(vec1, vec2))
        magnitude1 = math.sqrt(sum(a * a for a in vec1))
        magnitude2 = math.sqrt(sum(a * a for a in vec2))
        
        if magnitude1 == 0 or magnitude2 == 0:
            return 0
        return dot_product / (magnitude1 * magnitude2)
    
    def search_similar_documents(self, query_text: str, top_k: int = 3) -> List[Tuple[str, float, Dict]]:
        """
        Search for similar documents based on query text
        In a real implementation, you'd generate embeddings for the query_text
        """
        print(f"🔍 Searching for: '{query_text}'")
        
        # Load index metadata
        index_metadata = self.load_index_metadata()
        if not index_metadata:
            return []
        
        # Generate query embedding (simulated - normally use same model as indexing)
        query_embedding = np.random.rand(384).tolist()
        
        results = []
        
        # Load and compare each vector
        for vector_id in index_metadata.get('vector_ids', []):
            vector_data = self.load_vector(vector_id)
            if not vector_data:
                continue
                
            # Calculate similarity
            similarity = self.cosine_similarity(query_embedding, vector_data['embedding'])
            
            results.append((
                vector_data['metadata']['filename'],
                similarity,
                vector_data['metadata']
            ))
        
        # Sort by similarity (descending)
        results.sort(key=lambda x: x[1], reverse=True)
        
        return results[:top_k]
    
    def filter_by_metadata(self, filters: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Filter documents by metadata criteria"""
        print(f"🔎 Filtering by metadata: {filters}")
        
        index_metadata = self.load_index_metadata()
        if not index_metadata:
            return []
        
        matching_docs = []
        
        for vector_id in index_metadata.get('vector_ids', []):
            vector_data = self.load_vector(vector_id)
            if not vector_data:
                continue
            
            # Check if document matches all filter criteria
            matches = True
            for key, value in filters.items():
                if key not in vector_data['metadata'] or vector_data['metadata'][key] != value:
                    matches = False
                    break
            
            if matches:
                matching_docs.append(vector_data)
        
        return matching_docs

def main():
    BUCKET_NAME = "my-vector-documents-bucket"
    REGION = "us-west-2"
    
    print("🔍 Document Vector Query Demo")
    print("=" * 50)
    
    query_engine = DocumentVectorQuery(BUCKET_NAME, REGION)
    
    # Load and display index info
    index_metadata = query_engine.load_index_metadata()
    print(f"\n📊 Vector Index: {index_metadata.get('index_name', 'Unknown')}")
    print(f"   Description: {index_metadata.get('description', 'N/A')}")
    print(f"   Total vectors: {index_metadata.get('total_vectors', 0)}")
    print(f"   Dimensions: {index_metadata.get('dimension', 0)}")
    
    # Example 1: Semantic search
    print("\n" + "="*50)
    print("Example 1: Semantic Search")
    print("="*50)
    
    query_results = query_engine.search_similar_documents("financial report revenue", top_k=3)
    
    print("\nTop similar documents:")
    for i, (filename, similarity, metadata) in enumerate(query_results, 1):
        print(f"\n{i}. {filename}")
        print(f"   Similarity: {similarity:.4f}")
        print(f"   Type: {metadata.get('document_type', 'Unknown')}")
        print(f"   Department: {metadata.get('department', 'Unknown')}")
        print(f"   Author: {metadata.get('author', 'Unknown')}")
    
    # Example 2: Metadata filtering
    print("\n" + "="*50)
    print("Example 2: Metadata Filtering")
    print("="*50)
    
    # Filter by document type
    finance_docs = query_engine.filter_by_metadata({"document_type": "financial_report"})
    print(f"\nFinancial reports found: {len(finance_docs)}")
    for doc in finance_docs:
        print(f"  - {doc['metadata']['filename']} ({doc['metadata']['created_date']})")
    
    # Filter by department
    product_docs = query_engine.filter_by_metadata({"department": "product"})
    print(f"\nProduct department documents: {len(product_docs)}")
    for doc in product_docs:
        print(f"  - {doc['metadata']['filename']} by {doc['metadata']['author']}")
    
    print("\n" + "="*50)
    print("✅ Query demo complete!")
    print("\nIn a production S3 Vectors setup:")
    print("1. Use real embedding models (Titan, Bedrock, etc.)")
    print("2. Use S3 Vectors QueryVectors API for optimized search")
    print("3. Leverage metadata filtering for precise results")
    print("4. Implement hybrid search combining semantic + keyword")

if __name__ == "__main__":
    main()
