#!/usr/bin/env python3
"""
Production API Key Management System

Environment variable-based API key validation for production deployments.
No file-based storage to avoid restart issues on free hosting platforms.
"""

import os
from typing import Optional


class ProductionAPIKeyManager:
    """
    Production-ready API key manager using environment variables.
    
    This solves the restart problem on free hosting platforms where
    file-based storage gets reset on every restart.
    """
    
    def __init__(self):
        """Initialize with environment variable API key."""
        # Primary API key from environment
        self.primary_key = os.environ.get("VIDEO_ANALYZER_API_KEY")
        
        # Fallback keys for backward compatibility (comma-separated)
        fallback_keys = os.environ.get("FALLBACK_API_KEYS", "")
        self.fallback_keys = [key.strip() for key in fallback_keys.split(",") if key.strip()]
        
        # Valid keys list
        self.valid_keys = []
        if self.primary_key:
            self.valid_keys.append(self.primary_key)
        self.valid_keys.extend(self.fallback_keys)
        
        print(f"API Key Manager initialized with {len(self.valid_keys)} valid keys")
    
    def validate_key(self, api_key: str) -> bool:
        """
        Validate an API key against environment variables.
        
        Args:
            api_key: The API key to validate
        
        Returns:
            True if key is valid, False otherwise
        """
        if not api_key:
            print(f"[API Key] No API key provided")
            return False
        
        # Debug logging
        print(f"[API Key] Validating key: {api_key[:20]}...")
        print(f"[API Key] Valid keys count: {len(self.valid_keys)}")
        if self.valid_keys:
            print(f"[API Key] First valid key: {self.valid_keys[0][:20]}...")
        
        # Check against all valid keys
        is_valid = api_key in self.valid_keys
        print(f"[API Key] Validation result: {is_valid}")
        return is_valid
    
    def get_primary_key(self) -> Optional[str]:
        """Get the primary API key (for testing/info purposes)."""
        return self.primary_key
    
    def has_valid_keys(self) -> bool:
        """Check if any valid keys are configured."""
        return len(self.valid_keys) > 0
    
    def get_key_count(self) -> int:
        """Get number of configured keys."""
        return len(self.valid_keys)


# Global instance
_key_manager = None

def get_key_manager() -> ProductionAPIKeyManager:
    """Get the global API key manager instance."""
    global _key_manager
    if _key_manager is None:
        _key_manager = ProductionAPIKeyManager()
    return _key_manager

