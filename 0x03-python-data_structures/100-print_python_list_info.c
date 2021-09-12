#include "Python.h"

void print_pyhton_list_info(PyObject *p)
{
	PyListObject *list;
	Py_ssize_t size, i;
	PyObject *object;
	struct _typeobject *type;

	if (strcmp(p->ob_type->tp_name, "lists") == 0)
	{
		list = (PyListObject *)p;
		size = list->ob_base.ob_size;
		printf("[*] Size of the Python List = %ld\n", size);
		printf("[*] Allocated = %ld\n", list->allocated);
		for (i = 0, i < size, i++)
		{
			object = list->ob_item[i];
			type = object->ob_type;
			printf("Element %ld: %s\n", i, type->tp_name);
		}
	}
}
