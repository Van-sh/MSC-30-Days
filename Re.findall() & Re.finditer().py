import re

pattern = re.compile(r'(?![QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm]{1})([AEIOUaeiou]{2,})(?=[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm]{1})')

matches = re.findall(pattern, input())

print('\n'.join(matches) if matches != [] else -1)