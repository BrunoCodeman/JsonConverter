#coding: utf-8
import json
import __builtin__
builtin_types = dir(__builtin__)

class JsonConverter:
    """
    class to convert object into json, no matter what.
    """
    def convert(self):
        props = {}
        total_class_attributes = dir(self)
        try:
            for i in total_class_attributes:
                self_attribute = self.__attr_cleaner(i, self)
                if self_attribute:
                    props[i] = self.__type_checking(self_attribute) #convert the object to dict if needed
        except Exception, e:
            print e
        return json.dumps(props)

    def __attr_cleaner(self,attr_name, instance):
        attr = getattr(instance,attr_name)
        return attr if '__' not in attr_name and not callable(attr) else None #skip dunders and methods



    def __type_checking(self,self_attribute):
        attr_name = self_attribute.__class__.__name__
        if  attr_name == 'list':
            return self.__list_checking(self_attribute)
        if  attr_name ==  'dict':
            return self.__dict_checking(self_attribute)
        if  attr_name in builtin_types:
            return self_attribute
        else:
            return self.__class_checking(self_attribute)


    def __list_checking(self, listobj):
        final_list = []
        for item in listobj:
            final_list.append(self.__type_checking(item))
        return final_list

    def __dict_checking(self, dictobj):
        final_dict = {}
        for item in dictobj:
            final_dict[item] = self.__type_checking(dictobj[item])
        return final_dict

    def __class_checking(self, classobj):
        try:
            temp_data = classobj.__dict__
            for item in temp_data.keys():
                if self.__attr_cleaner(item, classobj):
                    temp_data[item] = self.__type_checking(temp_data[item])
                else:
                    del temp_data[item]
            return temp_data
        except Exception, e:
            print('Error converting %s: %s' %(classobj, e))