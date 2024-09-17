tr = f"{file_size // 1024},{file_size % 1024}"

    # 获取文件的创建日期，构造新文件名中的日期部分
    file_creation_time = os.path.getctime(image_path)  # 获取文件创建时间
    file_create