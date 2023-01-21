import json
import requests
from config.config import Config
from loguru import logger


class Hasura:

    @staticmethod
    def save(headers, website_name):
        payload = {
            "query": """mutation insert_website_headers($object: website_headers_insert_input!) {
                              insert_website_headers_one(object: $object) {
                                headers
                                website_name
                              }
                            } 
                        """,
            "variables": {
                          "object": {
                              "headers": headers,
                              "website_name": website_name
                          }
                        }
        }
        headers = {
            'x-hasura-admin-secret': Config.HASURA_ADMIN_SECRET,
            'Content-Type': 'application/json'
        }

        response = requests.post(Config.HASURA_URL, json=payload, headers=headers)
        logger.debug(response.text)
