"""
import openai
print(openai.__file__)

from openai.error import OpenAIError, AuthenticationError, RateLimitError

try:
    raise OpenAIError("测试错误")
except OpenAIError as e:
    print(f"捕获到 OpenAIError: {e}")
python --version
"""
"""
import openai
import pkgutil

modules = [name for _, name, _ in pkgutil.iter_modules(openai.__path__)]
print("OpenAI 模块内容:", modules)
"""

from openai import OpenAIError, AuthenticationError, RateLimitError
