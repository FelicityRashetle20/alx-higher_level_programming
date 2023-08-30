#include <stdio.h>
#include <Python.h>

/**
 * print_python_list_info - prints the info in python file
 * @p: PyObject
 * Returns nothing
 */
void print_python_list_info(PyObject *p)
{
	long int weight, i;
	PyListObject *py_list;
	PyObject *item;

	weight = Py_SIZE(p);
	printf("[*] Size of the Python py_list = %ld\n", weight);

	py_list = (PyListObject *)p;
	printf("[*] Allocated = %ld\n", py_list->allocated);

	for (i = 0; i < weight; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
	}
}
