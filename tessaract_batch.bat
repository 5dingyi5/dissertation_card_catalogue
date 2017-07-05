@Echo off
Set _SourcePath=X:\OCR_Test_Samples\MainTitleCC_Sample_OriginalTIF\*.tif
Set _OutputPath=X:\OCR_Test_Samples\Tessaract_OCR\tessaract_mainTitle\
Set _Tesseract="C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"
For %%A in (%_SourcePath%) Do Echo Converting %%A...&%_Tesseract% %%A %_OutputPath%%%~nA
Set "_SourcePath="
Set "_OutputPath="
Set "_Tesseract="