# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: unversioned
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from __future__ import absolute_import

import os
import sys
import unittest

import k8sclient
from k8sclient.rest import ApiException
from k8sclient.apis.storage_v1beta1_api import StorageV1beta1Api


class TestStorageV1beta1Api(unittest.TestCase):
    """ StorageV1beta1Api unit test stubs """

    def setUp(self):
        self.api = k8sclient.apis.storage_v1beta1_api.StorageV1beta1Api()

    def tearDown(self):
        pass

    def test_create_storage_class(self):
        """
        Test case for create_storage_class

        
        """
        pass

    def test_delete_collection_storage_class(self):
        """
        Test case for delete_collection_storage_class

        
        """
        pass

    def test_delete_storage_class(self):
        """
        Test case for delete_storage_class

        
        """
        pass

    def test_get_api_resources(self):
        """
        Test case for get_api_resources

        
        """
        pass

    def test_list_storage_class(self):
        """
        Test case for list_storage_class

        
        """
        pass

    def test_patch_storage_class(self):
        """
        Test case for patch_storage_class

        
        """
        pass

    def test_read_storage_class(self):
        """
        Test case for read_storage_class

        
        """
        pass

    def test_replace_storage_class(self):
        """
        Test case for replace_storage_class

        
        """
        pass

    def test_watch_storage_class(self):
        """
        Test case for watch_storage_class

        
        """
        pass

    def test_watch_storage_class_list(self):
        """
        Test case for watch_storage_class_list

        
        """
        pass


if __name__ == '__main__':
    unittest.main()
