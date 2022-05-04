#include <Python.h>
#include <object.h>
#include <listobject.h>

void print_python_list_info(PyObject *p)
{

	size_t size = PyList_Size(p);
	int idx;
	PyListObject *ob = (PyListObject *p);

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", ob->allocated);
	for (idx = 0; idx < size; idx++)
	{
		printf("Element %ld: %s\n",
		       idx,
		       (PY_TYPE(ob->ob_item[idx])->tp_name);
	}
}
