import ddddocr
import io
import time
from log import get_logger


logger = get_logger()
ocr = ddddocr.DdddOcr(beta=True)  # ocr模型

def ocr_recognize(image:bytes) -> str:
    """验证码识别

    Args:
        image (bytes): 打开的图像文件bytes

    Returns:
        str: 验证码结果
    """
    start_time = time.time()
    io.BytesIO().read()
    res = ocr.classification(image)
    cost_time = time.time() - start_time
    logger.info(f"ocr耗时: {format(cost_time * 1000, '.1f')} ms, 识别结果: {res}")
    return res

if __name__ == "__main__":
    file = "test.png"
    with open(file, 'rb') as f:
        res = ocr_recognize(f.read())
        print(res)