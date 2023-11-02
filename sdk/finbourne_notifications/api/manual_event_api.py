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

from pydantic import validate_arguments, ValidationError
from typing import overload, Optional, Union, Awaitable

from typing_extensions import Annotated
from pydantic import Field

from finbourne_notifications.models.manual_event import ManualEvent
from finbourne_notifications.models.manual_event_request import ManualEventRequest

from finbourne_notifications.api_client import ApiClient
from finbourne_notifications.api_response import ApiResponse
from finbourne_notifications.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class ManualEventApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @overload
    async def trigger_manual_event(self, manual_event_request : Annotated[ManualEventRequest, Field(..., description="The data required to trigger a manual event.")], **kwargs) -> ManualEvent:  # noqa: E501
        ...

    @overload
    def trigger_manual_event(self, manual_event_request : Annotated[ManualEventRequest, Field(..., description="The data required to trigger a manual event.")], async_req: Optional[bool]=True, **kwargs) -> ManualEvent:  # noqa: E501
        ...

    @validate_arguments
    def trigger_manual_event(self, manual_event_request : Annotated[ManualEventRequest, Field(..., description="The data required to trigger a manual event.")], async_req: Optional[bool]=None, **kwargs) -> Union[ManualEvent, Awaitable[ManualEvent]]:  # noqa: E501
        """[EXPERIMENTAL] TriggerManualEvent: Trigger a manual event.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.trigger_manual_event(manual_event_request, async_req=True)
        >>> result = thread.get()

        :param manual_event_request: The data required to trigger a manual event. (required)
        :type manual_event_request: ManualEventRequest
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: ManualEvent
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the trigger_manual_event_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        if async_req is not None:
            kwargs['async_req'] = async_req
        return self.trigger_manual_event_with_http_info(manual_event_request, **kwargs)  # noqa: E501

    @validate_arguments
    def trigger_manual_event_with_http_info(self, manual_event_request : Annotated[ManualEventRequest, Field(..., description="The data required to trigger a manual event.")], **kwargs) -> ApiResponse:  # noqa: E501
        """[EXPERIMENTAL] TriggerManualEvent: Trigger a manual event.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.trigger_manual_event_with_http_info(manual_event_request, async_req=True)
        >>> result = thread.get()

        :param manual_event_request: The data required to trigger a manual event. (required)
        :type manual_event_request: ManualEventRequest
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
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(ManualEvent, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'manual_event_request'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method trigger_manual_event" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params['manual_event_request'] is not None:
            _body_params = _params['manual_event_request']

        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # set the HTTP header `Content-Type`
        _content_types_list = _params.get('_content_type',
            self.api_client.select_header_content_type(
                ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json']))
        if _content_types_list:
                _header_params['Content-Type'] = _content_types_list

        # authentication setting
        _auth_settings = ['oauth2']  # noqa: E501

        _response_types_map = {
            '201': "ManualEvent",
            '400': "LusidValidationProblemDetails",
        }

        return self.api_client.call_api(
            '/api/manualevent', 'POST',
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
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))
