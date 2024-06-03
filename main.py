import os


cubism_sdk_for_native_zip = '/Users/dywang/Downloads/CubismSdkForNative-5-r.1.zip'
target_unzip_dir = '/Users/dywang/Desktop/tmp'

os.system('rm -rf {}/CubismSdkForNative-5-r.1'.format(target_unzip_dir))

os.system('unzip {} -d {}'.format(cubism_sdk_for_native_zip, target_unzip_dir))

# 删除不需要的文件
os.system('rm -rf {}/CubismSdkForNative-5-r.1/Samples/Cocos2d-x'.format(target_unzip_dir))
os.system('rm -rf {}/CubismSdkForNative-5-r.1/Samples/D3D9'.format(target_unzip_dir))
os.system('rm -rf {}/CubismSdkForNative-5-r.1/Samples/D3D11'.format(target_unzip_dir))
os.system('rm -rf {}/CubismSdkForNative-5-r.1/Samples/OpenGL'.format(target_unzip_dir))
os.system('rm -rf {}/CubismSdkForNative-5-r.1/Samples/Vulkan'.format(target_unzip_dir))

os.system('cd {}/CubismSdkForNative-5-r.1/Samples/Metal/thirdParty/scripts/ && ./setup_ios_cmake'.format(target_unzip_dir))
os.system('cd {}/CubismSdkForNative-5-r.1/Samples/Metal/Demo/proj.ios.cmake/scripts/ && ./proj_xcode'.format(target_unzip_dir))



# 把文件从/Users/dywang/Desktop/CubismSdkForNative-5-r.1/Framework/ 移动到 /Users/dywang/Desktop/CubismSdkForNative-5-r.1/Samples/Metal/Demo/proj.ios.cmake/build/proj_xcode_iphoneos/Framework/
os.system('cp -rf {}/CubismSdkForNative-5-r.1/Framework {}/CubismSdkForNative-5-r.1/Samples/Metal/Demo/proj.ios.cmake/build/proj_xcode_iphoneos/'.format(target_unzip_dir, target_unzip_dir))
os.system('rm -rf {}/CubismSdkForNative-5-r.1/Framework'.format(target_unzip_dir))

# /Users/dywang/Desktop/CubismSdkForNative-5-r.1/Core/ -> /Users/dywang/Desktop/CubismSdkForNative-5-r.1/Samples/Metal/Demo/proj.ios.cmake/build/proj_xcode_iphoneos/Core/
os.system('cp -rf {}/CubismSdkForNative-5-r.1/Core {}/CubismSdkForNative-5-r.1/Samples/Metal/Demo/proj.ios.cmake/build/proj_xcode_iphoneos/'.format(target_unzip_dir, target_unzip_dir))
os.system('rm -rf {}/CubismSdkForNative-5-r.1/Core'.format(target_unzip_dir))

# /Users/dywang/Desktop/CubismSdkForNative-5-r.1/Samples/Resources -> /Users/dywang/Desktop/CubismSdkForNative-5-r.1/Samples/Metal/Demo/proj.ios.cmake/build/proj_xcode_iphoneos/Resources
os.system('cp -rf {}/CubismSdkForNative-5-r.1/Samples/Resources {}/CubismSdkForNative-5-r.1/Samples/Metal/Demo/proj.ios.cmake/build/proj_xcode_iphoneos/'.format(target_unzip_dir, target_unzip_dir))
os.system('rm -rf {}/CubismSdkForNative-5-r.1/Samples/Resources'.format(target_unzip_dir))

# thirdParty/ -> /Users/dywang/Desktop/CubismSdkForNative-5-r.1/Samples/Metal/Demo/proj.ios.cmake/build/proj_xcode_iphoneos/thirdParty/
os.system('cp -rf {}/CubismSdkForNative-5-r.1/Samples/Metal/thirdParty {}/CubismSdkForNative-5-r.1/Samples/Metal/Demo/proj.ios.cmake/build/proj_xcode_iphoneos/'.format(target_unzip_dir, target_unzip_dir))
os.system('rm -rf {}/CubismSdkForNative-5-r.1/Samples/Metal/thirdParty'.format(target_unzip_dir))

# /Users/dywang/Desktop/tmp/CubismSdkForNative-5-r.1/Samples/Metal/Demo/proj.ios.cmake/src
os.system('cp -rf {}/CubismSdkForNative-5-r.1/Samples/Metal/Demo/proj.ios.cmake/src {}/CubismSdkForNative-5-r.1/Samples/Metal/Demo/proj.ios.cmake/build/proj_xcode_iphoneos/'.format(target_unzip_dir, target_unzip_dir))
os.system('rm -rf {}/CubismSdkForNative-5-r.1/Samples/Metal/Demo/proj.ios.cmake/src'.format(target_unzip_dir))



# /Users/dywang/Desktop/CubismSdkForNative-5-r.1/Samples/Metal/Demo/proj.ios.cmake/src/ -> /Users/dywang/Desktop/CubismSdkForNative-5-r.1/Samples/Metal/Demo/proj.ios.cmake/build/proj_xcode_iphoneos/src/

def read_write_file(file):
    with open(file, 'r') as f:
        content = f.read()
        content = content.replace('{}/CubismSdkForNative-5-r.1/Framework'.format(target_unzip_dir), '{}/CubismSdkForNative-5-r.1/Samples/Metal/Demo/proj.ios.cmake/build/proj_xcode_iphoneos/Framework'.format(target_unzip_dir))
        content = content.replace('{}/CubismSdkForNative-5-r.1/Core'.format(target_unzip_dir), '{}/CubismSdkForNative-5-r.1/Samples/Metal/Demo/proj.ios.cmake/build/proj_xcode_iphoneos/Core'.format(target_unzip_dir))
        content = content.replace('{}/CubismSdkForNative-5-r.1/Samples/Resources'.format(target_unzip_dir), '{}/CubismSdkForNative-5-r.1/Samples/Metal/Demo/proj.ios.cmake/build/proj_xcode_iphoneos/Resources'.format(target_unzip_dir))
        # /Users/dywang/Desktop/tmp/CubismSdkForNative-5-r.1/Samples/Metal/Demo/proj.ios.cmake/../../../../Core
        content = content.replace('{}/CubismSdkForNative-5-r.1/Samples/Metal/Demo/proj.ios.cmake/../../../../Core'.format(target_unzip_dir), '{}/CubismSdkForNative-5-r.1/Samples/Metal/Demo/proj.ios.cmake/build/proj_xcode_iphoneos/Core'.format(target_unzip_dir))
        content = content.replace('{}/CubismSdkForNative-5-r.1/Samples/Metal/Demo/proj.ios.cmake/../../../../Samples/Metal/thirdParty/'.format(target_unzip_dir), '{}/CubismSdkForNative-5-r.1/Samples/Metal/Demo/proj.ios.cmake/build/proj_xcode_iphoneos/thirdParty/'.format(target_unzip_dir))
        content = content.replace('{}/CubismSdkForNative-5-r.1/Samples/Metal/Demo/proj.ios.cmake/src/Info.plist'.format(target_unzip_dir), '{}/CubismSdkForNative-5-r.1/Samples/Metal/Demo/proj.ios.cmake/build/proj_xcode_iphoneos/src/Info.plist'.format(target_unzip_dir))
        content = content.replace('projectDirPath = "{}/CubismSdkForNative-5-r.1/Samples/Metal/Demo/proj.ios.cmake";'.format(target_unzip_dir), 'projectDirPath = "";')
        # INFOPLIST_FILE = "/Users/dywang/Desktop/tmp/CubismSdkForNative-5-r.1/Samples/Metal/Demo/proj.ios.cmake/build/proj_xcode_iphoneos/src/Info.plist";
        content = content.replace('INFOPLIST_FILE = "{}/CubismSdkForNative-5-r.1/Samples/Metal/Demo/proj.ios.cmake/build/proj_xcode_iphoneos/src/Info.plist";'.format(target_unzip_dir), 'INFOPLIST_FILE = "src/Info.plist";')
    with open(file, 'w') as f:
        f.write(content)

read_write_file('{}/CubismSdkForNative-5-r.1/Samples/Metal/Demo/proj.ios.cmake/build/proj_xcode_iphoneos/Demo.xcodeproj/project.pbxproj'.format(target_unzip_dir))

# 按行读取文件
with open('{}/CubismSdkForNative-5-r.1/Samples/Metal/Demo/proj.ios.cmake/build/proj_xcode_iphoneos/Demo.xcodeproj/project.pbxproj'.format(target_unzip_dir), 'r') as f:
    edit_lines = []
    lines = f.readlines()
    for line in lines:
        # 		fileEncoding = 4; name = LAppPal.mm; path = src/LAppPal.mm; sourceTree = SOURCE_ROOT; };
        if '; path = src/' in line and 'sourceTree = SOURCE_ROOT;' in line:
            src_path = '{}/CubismSdkForNative-5-r.1/Samples/Metal/Demo/proj.ios.cmake/build/proj_xcode_iphoneos/src/'.format(target_unzip_dir)
            line = line.replace('; path = src/', '; path = "{}'.format(src_path))
            line = line.replace('; sourceTree =', '"; sourceTree =')
            line = line.replace('sourceTree = SOURCE_ROOT;', 'sourceTree = "<absolute>";')
            edit_lines.append(line)
        else:
            edit_lines.append(line)
    # 把lines写入到文件中
    with open('{}/CubismSdkForNative-5-r.1/Samples/Metal/Demo/proj.ios.cmake/build/proj_xcode_iphoneos/Demo.xcodeproj/project.pbxproj'.format(target_unzip_dir), 'w') as f:
        f.writelines(edit_lines)

with open('{}/CubismSdkForNative-5-r.1/Samples/Metal/Demo/proj.ios.cmake/build/proj_xcode_iphoneos/Demo.xcodeproj/project.pbxproj'.format(target_unzip_dir), 'r') as f:
    edit_lines = []
    lines = f.readlines()
    for line in lines:
        # 		fileEncoding = 4; name = LAppPal.mm; path = src/LAppPal.mm; sourceTree = SOURCE_ROOT; };
        if 'sourceTree = "<absolute>"' in line:
            line = line.replace('{}/CubismSdkForNative-5-r.1/Samples/Metal/Demo/proj.ios.cmake/build/proj_xcode_iphoneos/'.format(target_unzip_dir), "")
            line = line.replace('sourceTree = "<absolute>"', 'sourceTree = SOURCE_ROOT')
        elif 'sourceTree = SOURCE_ROOT' in line:
            line = line.replace('path = build/proj_xcode_iphoneos/', 'path = ')
        edit_lines.append(line)
    # 把lines写入到文件中
    with open('{}/CubismSdkForNative-5-r.1/Samples/Metal/Demo/proj.ios.cmake/build/proj_xcode_iphoneos/Demo.xcodeproj/project.pbxproj'.format(target_unzip_dir), 'w') as f:
        f.writelines(edit_lines)


with open('{}/CubismSdkForNative-5-r.1/Samples/Metal/Demo/proj.ios.cmake/build/proj_xcode_iphoneos/Demo.xcodeproj/project.pbxproj'.format(target_unzip_dir), 'r') as f:
    content = f.read()
    content = content.replace('{}/CubismSdkForNative-5-r.1/Samples/Metal/Demo/proj.ios.cmake/build/proj_xcode_iphoneos/'.format(target_unzip_dir), '')
    content = content.replace('{}/CubismSdkForNative-5-r.1/Samples/Metal/Demo/proj.ios.cmake/src/'.format(target_unzip_dir), 'src/')
with open('{}/CubismSdkForNative-5-r.1/Samples/Metal/Demo/proj.ios.cmake/build/proj_xcode_iphoneos/Demo.xcodeproj/project.pbxproj'.format(target_unzip_dir), 'w') as f:
    f.write(content)

