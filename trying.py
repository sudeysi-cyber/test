import subprocess

file1 = 'file1.txt'
file2 = 'file2.txt'
output_file = 'new.patch'
output_file2 = 'fixed.patch'
# result = subprocess.run(['git', 'diff', file1, file2], capture_output=True, text=True).stdout
# print(result)

def diff(file1,file2,output_file):
    cmd = ['git', 'diff',f'--output={output_file}', file1, file2]
    #cmd = ['git', 'diff','--index','-P',f'--output={output_file}', file1, file2]
    #cmd = ['git', 'diff', '--patience', file1, file2]
    process = subprocess.run(cmd, capture_output=True, text=True).stdout
    #process = subprocess.run(['git', 'diff', file1, file2],capture_output=True, text=True).stdout
    print(process)
    return process

def apply_diff(diff_file):
    cmd = ['git', 'apply', diff_file]
    process2 = subprocess.run(cmd, capture_output=True, text=True).stdout
    print(process2)
    return process2
def main():
    result = diff(file1, file2, output_file)
    apply_difference = apply_diff(output_file)
    print(apply_difference)
    return apply_difference

if __name__ == "__main__":
    main()



