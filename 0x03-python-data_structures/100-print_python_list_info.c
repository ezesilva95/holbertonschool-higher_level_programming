#include <Python.h>
#include <listobject.h>
#include <object.h>

void print_python_list_info(PyObject *p)
{
	idx = 0;
	int size = PyList_Size(p);
	alloc = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %li\n", size);
	printf("[*] Allocated = %li\n", alloc);
	for (idx = 0; idx < size; idx++)
		printf("Element %li: %s\n", idx, 
				PyList_GetItem(p, idx)->ob_type->tp_name);
}
