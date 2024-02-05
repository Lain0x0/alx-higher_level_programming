#include <Python.h>
#include <stdio.h>

/**
 * print_python_list - Print information about a Python list.
 * @p: Pointer to PyObject representing a list.
 */
void print_python_list(PyObject *p)
{
	if (!PyList_Check(p))
	{
		fprintf(stderr, "Invalid PyListObject\n");
		return;
	}

	printf("[*] Python list info\n");
	printf("Size of the Python List = %ld\n", PyList_Size(p));
	printf("Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (Py_ssize_t i = 0; i < PyList_Size(p); ++i)
	{
		PyObject *elem = PyList_GetItem(p, i);

		printf("Element %ld: %s\n", i, Py_TYPE(elem)->tp_name);
	}
}

/**
 * print_python_bytes - Print information about a Python bytes object.
 * @p: Pointer to PyObject representing bytes.
 */
void print_python_bytes(PyObject *p)
{
	if (!PyBytes_Check(p))
	{
		fprintf(stderr, "Invalid PyBytesObject\n");
		return;
	}

	printf("[.] bytes object info\n");
	printf("size: %ld\n", PyBytes_Size(p));

	printf("trying string: ");
	Py_ssize_t size = PyBytes_Size(p);

	char *str = PyBytes_AsString(p);

	for (Py_ssize_t i = 0; i < size && i < 10; ++i)
	{
		printf("%02x ", (unsigned char)str[i]);
	}
	printf("\n");
}

/**
 * print_python_float - Print information about a Python float object.
 * @p: Pointer to PyObject representing float.
 */
void print_python_float(PyObject *p)
{
	if (!PyFloat_Check(p))
	{
		fprintf(stderr, "Invalid PyFloatObject\n");
		return;
	}

	printf("[.] float object info\n");
	printf("value: %f\n", ((PyFloatObject *)p)->ob_fval);
}

/**
 * main - Example usage.
 * Return: 0 on success.
 */
int main(void)
{

	Py_Initialize();
	PyObject *list = PyList_New(5);
	PyObject *bytes_obj = PyBytes_FromString("Hello, world!");
	PyObject *float_obj = PyFloat_FromDouble(3.14);

	print_python_list(list);
	print_python_bytes(bytes_obj);
	print_python_float(float_obj);

	Py_DECREF(list);
	Py_DECREF(bytes_obj);
	Py_DECREF(float_obj);

	Py_Finalize();

	return (0);
}

