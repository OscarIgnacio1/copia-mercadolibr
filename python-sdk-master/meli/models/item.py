# coding: utf-8

"""
    MELI Markeplace SDK

    This is a the codebase to generate a SDK for Open Platform Marketplace  # noqa: E501

    The version of the OpenAPI document: 3.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from meli.configuration import Configuration


class Item(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'title': 'str',
        'category_id': 'str',
        'price': 'int',
        'currency_id': 'str',
        'available_quantity': 'str',
        'buying_mode': 'str',
        'listing_type_id': 'str',
        'condition': 'str',
        'description': 'str',
        'video_id': 'str',
        'pictures': 'list[ItemPictures]',
        'attributes': 'list[Attributes]',
        'variations': 'list[Variations]'
    }

    attribute_map = {
        'title': 'title',
        'category_id': 'category_id',
        'price': 'price',
        'currency_id': 'currency_id',
        'available_quantity': 'available_quantity',
        'buying_mode': 'buying_mode',
        'listing_type_id': 'listing_type_id',
        'condition': 'condition',
        'description': 'description',
        'video_id': 'video_id',
        'pictures': 'pictures',
        'attributes': 'attributes',
        'variations': 'variations'
    }

    def __init__(self, title=None, category_id=None, price=None, currency_id=None, available_quantity=None, buying_mode=None, listing_type_id=None, condition=None, description=None, video_id=None, pictures=None, attributes=None, variations=None, local_vars_configuration=None):  # noqa: E501
        """Item - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._title = None
        self._category_id = None
        self._price = None
        self._currency_id = None
        self._available_quantity = None
        self._buying_mode = None
        self._listing_type_id = None
        self._condition = None
        self._description = None
        self._video_id = None
        self._pictures = None
        self._attributes = None
        self._variations = None
        self.discriminator = None

        self.title = title
        self.category_id = category_id
        self.price = price
        self.currency_id = currency_id
        self.available_quantity = available_quantity
        self.buying_mode = buying_mode
        self.listing_type_id = listing_type_id
        self.condition = condition
        self.description = description
        self.video_id = video_id
        self.pictures = pictures
        if attributes is not None:
            self.attributes = attributes
        if variations is not None:
            self.variations = variations

    @property
    def title(self):
        """Gets the title of this Item.  # noqa: E501


        :return: The title of this Item.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this Item.


        :param title: The title of this Item.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and title is None:  # noqa: E501
            raise ValueError("Invalid value for `title`, must not be `None`")  # noqa: E501

        self._title = title

    @property
    def category_id(self):
        """Gets the category_id of this Item.  # noqa: E501


        :return: The category_id of this Item.  # noqa: E501
        :rtype: str
        """
        return self._category_id

    @category_id.setter
    def category_id(self, category_id):
        """Sets the category_id of this Item.


        :param category_id: The category_id of this Item.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and category_id is None:  # noqa: E501
            raise ValueError("Invalid value for `category_id`, must not be `None`")  # noqa: E501

        self._category_id = category_id

    @property
    def price(self):
        """Gets the price of this Item.  # noqa: E501


        :return: The price of this Item.  # noqa: E501
        :rtype: int
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this Item.


        :param price: The price of this Item.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and price is None:  # noqa: E501
            raise ValueError("Invalid value for `price`, must not be `None`")  # noqa: E501

        self._price = price

    @property
    def currency_id(self):
        """Gets the currency_id of this Item.  # noqa: E501


        :return: The currency_id of this Item.  # noqa: E501
        :rtype: str
        """
        return self._currency_id

    @currency_id.setter
    def currency_id(self, currency_id):
        """Sets the currency_id of this Item.


        :param currency_id: The currency_id of this Item.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and currency_id is None:  # noqa: E501
            raise ValueError("Invalid value for `currency_id`, must not be `None`")  # noqa: E501

        self._currency_id = currency_id

    @property
    def available_quantity(self):
        """Gets the available_quantity of this Item.  # noqa: E501


        :return: The available_quantity of this Item.  # noqa: E501
        :rtype: str
        """
        return self._available_quantity

    @available_quantity.setter
    def available_quantity(self, available_quantity):
        """Sets the available_quantity of this Item.


        :param available_quantity: The available_quantity of this Item.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and available_quantity is None:  # noqa: E501
            raise ValueError("Invalid value for `available_quantity`, must not be `None`")  # noqa: E501

        self._available_quantity = available_quantity

    @property
    def buying_mode(self):
        """Gets the buying_mode of this Item.  # noqa: E501


        :return: The buying_mode of this Item.  # noqa: E501
        :rtype: str
        """
        return self._buying_mode

    @buying_mode.setter
    def buying_mode(self, buying_mode):
        """Sets the buying_mode of this Item.


        :param buying_mode: The buying_mode of this Item.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and buying_mode is None:  # noqa: E501
            raise ValueError("Invalid value for `buying_mode`, must not be `None`")  # noqa: E501

        self._buying_mode = buying_mode

    @property
    def listing_type_id(self):
        """Gets the listing_type_id of this Item.  # noqa: E501


        :return: The listing_type_id of this Item.  # noqa: E501
        :rtype: str
        """
        return self._listing_type_id

    @listing_type_id.setter
    def listing_type_id(self, listing_type_id):
        """Sets the listing_type_id of this Item.


        :param listing_type_id: The listing_type_id of this Item.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and listing_type_id is None:  # noqa: E501
            raise ValueError("Invalid value for `listing_type_id`, must not be `None`")  # noqa: E501

        self._listing_type_id = listing_type_id

    @property
    def condition(self):
        """Gets the condition of this Item.  # noqa: E501


        :return: The condition of this Item.  # noqa: E501
        :rtype: str
        """
        return self._condition

    @condition.setter
    def condition(self, condition):
        """Sets the condition of this Item.


        :param condition: The condition of this Item.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and condition is None:  # noqa: E501
            raise ValueError("Invalid value for `condition`, must not be `None`")  # noqa: E501

        self._condition = condition

    @property
    def description(self):
        """Gets the description of this Item.  # noqa: E501


        :return: The description of this Item.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Item.


        :param description: The description of this Item.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and description is None:  # noqa: E501
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def video_id(self):
        """Gets the video_id of this Item.  # noqa: E501


        :return: The video_id of this Item.  # noqa: E501
        :rtype: str
        """
        return self._video_id

    @video_id.setter
    def video_id(self, video_id):
        """Sets the video_id of this Item.


        :param video_id: The video_id of this Item.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and video_id is None:  # noqa: E501
            raise ValueError("Invalid value for `video_id`, must not be `None`")  # noqa: E501

        self._video_id = video_id

    @property
    def pictures(self):
        """Gets the pictures of this Item.  # noqa: E501


        :return: The pictures of this Item.  # noqa: E501
        :rtype: list[ItemPictures]
        """
        return self._pictures

    @pictures.setter
    def pictures(self, pictures):
        """Sets the pictures of this Item.


        :param pictures: The pictures of this Item.  # noqa: E501
        :type: list[ItemPictures]
        """
        if self.local_vars_configuration.client_side_validation and pictures is None:  # noqa: E501
            raise ValueError("Invalid value for `pictures`, must not be `None`")  # noqa: E501

        self._pictures = pictures

    @property
    def attributes(self):
        """Gets the attributes of this Item.  # noqa: E501


        :return: The attributes of this Item.  # noqa: E501
        :rtype: list[Attributes]
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this Item.


        :param attributes: The attributes of this Item.  # noqa: E501
        :type: list[Attributes]
        """

        self._attributes = attributes

    @property
    def variations(self):
        """Gets the variations of this Item.  # noqa: E501


        :return: The variations of this Item.  # noqa: E501
        :rtype: list[Variations]
        """
        return self._variations

    @variations.setter
    def variations(self, variations):
        """Sets the variations of this Item.


        :param variations: The variations of this Item.  # noqa: E501
        :type: list[Variations]
        """

        self._variations = variations

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Item):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Item):
            return True

        return self.to_dict() != other.to_dict()