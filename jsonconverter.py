#coding: utf-8
import __builtin__
builtin_types = dir(__builtin__)

class JsonConverter:
    """
    class to convert object into json, no matter what.
    """
    def convert(self):
        props = dict()
        total_class_attributes = dir(self)
        try:
            for i in total_class_attributes:
                self_attribute = self.__attr_cleaner(i, self)
                if self_attribute:
                    print('analyzing %s' % i)
                    print("%s will be converted" % i)
                    props[i] = self.__type_checking(self_attribute) #convert the object to dict if needed
                    print('props["%s"]: %s' %(i,props[i]))
                else:
                    print('%s will not be processed' % i)
        except Exception, e:
            print e
        return props

    def __attr_cleaner(self,attr_name, instance):
        attr = getattr(instance,attr_name)
        if '__' not in attr_name and not callable(attr): #skip dunders and methods
            return attr


    def __type_checking(self,self_attribute):
        print('self_attribute: %s' % self_attribute)
        if self_attribute.__class__.__name__ == 'list':
            print('%s is a list' % self_attribute)
            return self.__list_checking(self_attribute)
        if self_attribute.__class__.__name__ == 'dict':
            print('%s is a dict' % self_attribute)
            return self.__dict_checking(self_attribute)
        if self_attribute.__class__.__name__ in builtin_types:
            print('%s is a builtin type' % self_attribute)
            return self_attribute
        else:
            print('%s is not a builtin type, list or dict. Converting...' % self_attribute.__class__.__name__)
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
            print('temp data of object: %s' %temp_data)
            for item in temp_data.keys():
                if self.__attr_cleaner(item, classobj):
                    temp_data[item] = self.__type_checking(temp_data[item])
                    print('temp_data["%s"]: %s' %(item,temp_data[item]))
                else:
                    del temp_data[item]
            return temp_data
        except Exception, e:
            print('Error converting %s: %s' %(classobj, e))