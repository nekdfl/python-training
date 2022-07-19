##
## Auto Generated makefile by CodeLite IDE
## any manual changes will be erased      
##
## Debug
ProjectName            :=cpp
ConfigurationName      :=Debug
WorkspaceConfiguration := $(ConfigurationName)
WorkspacePath          :=/home/nek/projects/python-training/lesson7/cpp
ProjectPath            :=/home/nek/projects/python-training/lesson7/cpp/cpp
IntermediateDirectory  :=../build-$(ConfigurationName)/cpp
OutDir                 :=../build-$(ConfigurationName)/cpp
CurrentFileName        :=
CurrentFilePath        :=
CurrentFileFullPath    :=
User                   :=nek
Date                   :=19/07/22
CodeLitePath           :=/home/nek/.codelite
LinkerName             :=/usr/bin/g++
SharedObjectLinkerName :=/usr/bin/g++ -shared -fPIC
ObjectSuffix           :=.o
DependSuffix           :=.o.d
PreprocessSuffix       :=.i
DebugSwitch            :=-g 
IncludeSwitch          :=-I
LibrarySwitch          :=-l
OutputSwitch           :=-o 
LibraryPathSwitch      :=-L
PreprocessorSwitch     :=-D
SourceSwitch           :=-c 
OutputFile             :=../build-$(ConfigurationName)/bin/$(ProjectName)
Preprocessors          :=
ObjectSwitch           :=-o 
ArchiveOutputSwitch    := 
PreprocessOnlySwitch   :=-E
ObjectsFileList        :=$(IntermediateDirectory)/ObjectsList.txt
PCHCompileFlags        :=
LinkOptions            :=  
IncludePath            :=  $(IncludeSwitch). $(IncludeSwitch). 
IncludePCH             := 
RcIncludePath          := 
Libs                   := 
ArLibs                 :=  
LibPath                := $(LibraryPathSwitch). 

##
## Common variables
## AR, CXX, CC, AS, CXXFLAGS and CFLAGS can be overriden using an environment variables
##
AR       := /usr/bin/ar rcu
CXX      := /usr/bin/g++
CC       := /usr/bin/gcc
CXXFLAGS :=  -g -O0 -Wall $(Preprocessors)
CFLAGS   :=  -g -O0 -Wall $(Preprocessors)
ASFLAGS  := 
AS       := /usr/bin/as


##
## User defined environment variables
##
CodeLiteDir:=/usr/share/codelite
Objects0=../build-$(ConfigurationName)/cpp/square.cpp$(ObjectSuffix) ../build-$(ConfigurationName)/cpp/triangle.cpp$(ObjectSuffix) ../build-$(ConfigurationName)/cpp/circle.cpp$(ObjectSuffix) ../build-$(ConfigurationName)/cpp/main.cpp$(ObjectSuffix) 



Objects=$(Objects0) 

##
## Main Build Targets 
##
.PHONY: all clean PreBuild PrePreBuild PostBuild MakeIntermediateDirs
all: MakeIntermediateDirs $(OutputFile)

$(OutputFile): ../build-$(ConfigurationName)/cpp/.d $(Objects) 
	@mkdir -p "../build-$(ConfigurationName)/cpp"
	@echo "" > $(IntermediateDirectory)/.d
	@echo $(Objects0)  > $(ObjectsFileList)
	$(LinkerName) $(OutputSwitch)$(OutputFile) @$(ObjectsFileList) $(LibPath) $(Libs) $(LinkOptions)

MakeIntermediateDirs:
	@mkdir -p "../build-$(ConfigurationName)/cpp"
	@mkdir -p ""../build-$(ConfigurationName)/bin""

../build-$(ConfigurationName)/cpp/.d:
	@mkdir -p "../build-$(ConfigurationName)/cpp"

PreBuild:


##
## Objects
##
../build-$(ConfigurationName)/cpp/square.cpp$(ObjectSuffix): square.cpp ../build-$(ConfigurationName)/cpp/square.cpp$(DependSuffix)
	$(CXX) $(IncludePCH) $(SourceSwitch) "/home/nek/projects/python-training/lesson7/cpp/cpp/square.cpp" $(CXXFLAGS) $(ObjectSwitch)$(IntermediateDirectory)/square.cpp$(ObjectSuffix) $(IncludePath)
../build-$(ConfigurationName)/cpp/square.cpp$(DependSuffix): square.cpp
	@$(CXX) $(CXXFLAGS) $(IncludePCH) $(IncludePath) -MG -MP -MT../build-$(ConfigurationName)/cpp/square.cpp$(ObjectSuffix) -MF../build-$(ConfigurationName)/cpp/square.cpp$(DependSuffix) -MM square.cpp

../build-$(ConfigurationName)/cpp/square.cpp$(PreprocessSuffix): square.cpp
	$(CXX) $(CXXFLAGS) $(IncludePCH) $(IncludePath) $(PreprocessOnlySwitch) $(OutputSwitch) ../build-$(ConfigurationName)/cpp/square.cpp$(PreprocessSuffix) square.cpp

../build-$(ConfigurationName)/cpp/triangle.cpp$(ObjectSuffix): triangle.cpp ../build-$(ConfigurationName)/cpp/triangle.cpp$(DependSuffix)
	$(CXX) $(IncludePCH) $(SourceSwitch) "/home/nek/projects/python-training/lesson7/cpp/cpp/triangle.cpp" $(CXXFLAGS) $(ObjectSwitch)$(IntermediateDirectory)/triangle.cpp$(ObjectSuffix) $(IncludePath)
../build-$(ConfigurationName)/cpp/triangle.cpp$(DependSuffix): triangle.cpp
	@$(CXX) $(CXXFLAGS) $(IncludePCH) $(IncludePath) -MG -MP -MT../build-$(ConfigurationName)/cpp/triangle.cpp$(ObjectSuffix) -MF../build-$(ConfigurationName)/cpp/triangle.cpp$(DependSuffix) -MM triangle.cpp

../build-$(ConfigurationName)/cpp/triangle.cpp$(PreprocessSuffix): triangle.cpp
	$(CXX) $(CXXFLAGS) $(IncludePCH) $(IncludePath) $(PreprocessOnlySwitch) $(OutputSwitch) ../build-$(ConfigurationName)/cpp/triangle.cpp$(PreprocessSuffix) triangle.cpp

../build-$(ConfigurationName)/cpp/circle.cpp$(ObjectSuffix): circle.cpp ../build-$(ConfigurationName)/cpp/circle.cpp$(DependSuffix)
	$(CXX) $(IncludePCH) $(SourceSwitch) "/home/nek/projects/python-training/lesson7/cpp/cpp/circle.cpp" $(CXXFLAGS) $(ObjectSwitch)$(IntermediateDirectory)/circle.cpp$(ObjectSuffix) $(IncludePath)
../build-$(ConfigurationName)/cpp/circle.cpp$(DependSuffix): circle.cpp
	@$(CXX) $(CXXFLAGS) $(IncludePCH) $(IncludePath) -MG -MP -MT../build-$(ConfigurationName)/cpp/circle.cpp$(ObjectSuffix) -MF../build-$(ConfigurationName)/cpp/circle.cpp$(DependSuffix) -MM circle.cpp

../build-$(ConfigurationName)/cpp/circle.cpp$(PreprocessSuffix): circle.cpp
	$(CXX) $(CXXFLAGS) $(IncludePCH) $(IncludePath) $(PreprocessOnlySwitch) $(OutputSwitch) ../build-$(ConfigurationName)/cpp/circle.cpp$(PreprocessSuffix) circle.cpp

../build-$(ConfigurationName)/cpp/main.cpp$(ObjectSuffix): main.cpp ../build-$(ConfigurationName)/cpp/main.cpp$(DependSuffix)
	$(CXX) $(IncludePCH) $(SourceSwitch) "/home/nek/projects/python-training/lesson7/cpp/cpp/main.cpp" $(CXXFLAGS) $(ObjectSwitch)$(IntermediateDirectory)/main.cpp$(ObjectSuffix) $(IncludePath)
../build-$(ConfigurationName)/cpp/main.cpp$(DependSuffix): main.cpp
	@$(CXX) $(CXXFLAGS) $(IncludePCH) $(IncludePath) -MG -MP -MT../build-$(ConfigurationName)/cpp/main.cpp$(ObjectSuffix) -MF../build-$(ConfigurationName)/cpp/main.cpp$(DependSuffix) -MM main.cpp

../build-$(ConfigurationName)/cpp/main.cpp$(PreprocessSuffix): main.cpp
	$(CXX) $(CXXFLAGS) $(IncludePCH) $(IncludePath) $(PreprocessOnlySwitch) $(OutputSwitch) ../build-$(ConfigurationName)/cpp/main.cpp$(PreprocessSuffix) main.cpp


-include ../build-$(ConfigurationName)/cpp//*$(DependSuffix)
##
## Clean
##
clean:
	$(RM) -r $(IntermediateDirectory)


