def heap_sort(arr):
    # Hàm để tạo một heap tối ưu từ một danh sách
    def heapify(arr, n, i):
        largest = i  # Khởi tạo largest là nút gốc
        l = 2 * i + 1  # Lấy chỉ số của nút con trái
        r = 2 * i + 2  # Lấy chỉ số của nút con phải

        # Nếu nút con trái lớn hơn nút gốc
        if l < n and arr[i] < arr[l]:
            largest = l

        # Nếu nút con phải lớn hơn nút gốc
        if r < n and arr[largest] < arr[r]:
            largest = r

        # Nếu largest không phải là nút gốc
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]  # Hoán đổi nút gốc và largest
            heapify(arr, n, largest)  # Tiếp tục tối ưu heap

    n = len(arr)

    # Xây dựng một heap tối ưu
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Trích xuất các phần tử một cách lần lượt từ heap
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]  # Hoán đổi phần tử đầu tiên và cuối cùng
        heapify(arr, i, 0)

    return arr