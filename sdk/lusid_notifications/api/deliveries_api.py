# coding: utf-8

"""
    FINBOURNE Notifications API

    FINBOURNE Technology  # noqa: E501

    Contact: info@finbourne.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import re  # noqa: F401
import io
import warnings

from pydantic.v1 import validate_arguments, ValidationError
from typing import overload, Optional, Union, Awaitable

from typing_extensions import Annotated
from pydantic.v1 import Field, StrictInt, constr, validator

from typing import Optional

from lusid_notifications.models.resource_list_of_delivery import ResourceListOfDelivery

from lusid_notifications.api_client import ApiClient
from lusid_notifications.api_response import ApiResponse
from lusid_notifications.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)
from lusid_notifications.extensions.configuration_options import ConfigurationOptions


class DeliveriesApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @overload
    async def list_deliveries(self, page : Annotated[Optional[constr(strict=True, max_length=500, min_length=1)], Field(description="The pagination token to use to continue listing delivery attempts. This value is returned from the previous call. When this field is supplied the filter field should not be supplied.")] = None, limit : Annotated[Optional[StrictInt], Field(description="The maximum number of delivery attempts to retrieve. Defaults to 200 if not specified.")] = None, filter : Annotated[Optional[constr(strict=True, max_length=16384, min_length=0)], Field(description="Expression to filter the result set. For more information about filtering results, see https://support.lusid.com/knowledgebase/article/KA-01914.  By default, we set this filter to only query for the last week's worth of Deliveries, however if a filter is explicitly set, this will be overriden.  An example filter to override the attempt time date might be 'AttemptTime gt 2023-08-25' for example")] = None, **kwargs) -> ResourceListOfDelivery:  # noqa: E501
        ...

    @overload
    def list_deliveries(self, page : Annotated[Optional[constr(strict=True, max_length=500, min_length=1)], Field(description="The pagination token to use to continue listing delivery attempts. This value is returned from the previous call. When this field is supplied the filter field should not be supplied.")] = None, limit : Annotated[Optional[StrictInt], Field(description="The maximum number of delivery attempts to retrieve. Defaults to 200 if not specified.")] = None, filter : Annotated[Optional[constr(strict=True, max_length=16384, min_length=0)], Field(description="Expression to filter the result set. For more information about filtering results, see https://support.lusid.com/knowledgebase/article/KA-01914.  By default, we set this filter to only query for the last week's worth of Deliveries, however if a filter is explicitly set, this will be overriden.  An example filter to override the attempt time date might be 'AttemptTime gt 2023-08-25' for example")] = None, async_req: Optional[bool]=True, **kwargs) -> ResourceListOfDelivery:  # noqa: E501
        ...

    @validate_arguments
    def list_deliveries(self, page : Annotated[Optional[constr(strict=True, max_length=500, min_length=1)], Field(description="The pagination token to use to continue listing delivery attempts. This value is returned from the previous call. When this field is supplied the filter field should not be supplied.")] = None, limit : Annotated[Optional[StrictInt], Field(description="The maximum number of delivery attempts to retrieve. Defaults to 200 if not specified.")] = None, filter : Annotated[Optional[constr(strict=True, max_length=16384, min_length=0)], Field(description="Expression to filter the result set. For more information about filtering results, see https://support.lusid.com/knowledgebase/article/KA-01914.  By default, we set this filter to only query for the last week's worth of Deliveries, however if a filter is explicitly set, this will be overriden.  An example filter to override the attempt time date might be 'AttemptTime gt 2023-08-25' for example")] = None, async_req: Optional[bool]=None, **kwargs) -> Union[ResourceListOfDelivery, Awaitable[ResourceListOfDelivery]]:  # noqa: E501
        """ListDeliveries: List Deliveries  # noqa: E501

        Currently only returns deliveries with failed attempts.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_deliveries(page, limit, filter, async_req=True)
        >>> result = thread.get()

        :param page: The pagination token to use to continue listing delivery attempts. This value is returned from the previous call. When this field is supplied the filter field should not be supplied.
        :type page: str
        :param limit: The maximum number of delivery attempts to retrieve. Defaults to 200 if not specified.
        :type limit: int
        :param filter: Expression to filter the result set. For more information about filtering results, see https://support.lusid.com/knowledgebase/article/KA-01914.  By default, we set this filter to only query for the last week's worth of Deliveries, however if a filter is explicitly set, this will be overriden.  An example filter to override the attempt time date might be 'AttemptTime gt 2023-08-25' for example
        :type filter: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: Timeout setting. Do not use - use the opts parameter instead
        :param opts: Configuration options for this request
        :type opts: ConfigurationOptions, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: ResourceListOfDelivery
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the list_deliveries_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        if async_req is not None:
            kwargs['async_req'] = async_req
        return self.list_deliveries_with_http_info(page, limit, filter, **kwargs)  # noqa: E501

    @validate_arguments
    def list_deliveries_with_http_info(self, page : Annotated[Optional[constr(strict=True, max_length=500, min_length=1)], Field(description="The pagination token to use to continue listing delivery attempts. This value is returned from the previous call. When this field is supplied the filter field should not be supplied.")] = None, limit : Annotated[Optional[StrictInt], Field(description="The maximum number of delivery attempts to retrieve. Defaults to 200 if not specified.")] = None, filter : Annotated[Optional[constr(strict=True, max_length=16384, min_length=0)], Field(description="Expression to filter the result set. For more information about filtering results, see https://support.lusid.com/knowledgebase/article/KA-01914.  By default, we set this filter to only query for the last week's worth of Deliveries, however if a filter is explicitly set, this will be overriden.  An example filter to override the attempt time date might be 'AttemptTime gt 2023-08-25' for example")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """ListDeliveries: List Deliveries  # noqa: E501

        Currently only returns deliveries with failed attempts.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_deliveries_with_http_info(page, limit, filter, async_req=True)
        >>> result = thread.get()

        :param page: The pagination token to use to continue listing delivery attempts. This value is returned from the previous call. When this field is supplied the filter field should not be supplied.
        :type page: str
        :param limit: The maximum number of delivery attempts to retrieve. Defaults to 200 if not specified.
        :type limit: int
        :param filter: Expression to filter the result set. For more information about filtering results, see https://support.lusid.com/knowledgebase/article/KA-01914.  By default, we set this filter to only query for the last week's worth of Deliveries, however if a filter is explicitly set, this will be overriden.  An example filter to override the attempt time date might be 'AttemptTime gt 2023-08-25' for example
        :type filter: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: Timeout setting. Do not use - use the opts parameter instead
        :param opts: Configuration options for this request
        :type opts: ConfigurationOptions, optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(ResourceListOfDelivery, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'page',
            'limit',
            'filter'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers',
                'opts'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_deliveries" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        if _params.get('page') is not None:  # noqa: E501
            _query_params.append(('page', _params['page']))

        if _params.get('limit') is not None:  # noqa: E501
            _query_params.append(('limit', _params['limit']))

        if _params.get('filter') is not None:  # noqa: E501
            _query_params.append(('filter', _params['filter']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['oauth2']  # noqa: E501

        _response_types_map = {
            '200': "ResourceListOfDelivery",
            '400': "LusidValidationProblemDetails",
            '404': "str",
        }

        return self.api_client.call_api(
            '/api/deliveries', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            opts=_params.get('opts'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))
