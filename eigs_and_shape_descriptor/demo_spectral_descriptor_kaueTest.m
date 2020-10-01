%function demo_spectral_descriptor_kaueTest
% 
% Chunyuan Li
% May 13, 2014

DATASET = 'SHREC2011_Nonrigid';  % dataset to process. 'PARAMETERS_test.m' 'SHREC2011_Nonrigid'

% set path for auxilary code
addpath(genpath(fullfile('sgwt_toolbox')));  % spectral graph wavelets code
addpath(fullfile('meshcodes'));              % basic mesh processing code


load('/Volumes/CipacProcessing/Projects/RF_KaueAlzheimers/descriptor/016_S_1326/016_S_1326x4.mat');     % load the eigenvalues and eigenfunction of mesh

FV = stlread('/Volumes/CipacProcessing/Projects/RF_KaueAlzheimers/brain_region_mat/016_S_1326/016_S_1326x4.stl');

vertices = FV.Points;
faces    = FV.ConnectivityList;

%descriptor.gps   = Get_Signature(evecs, evals, 'GPS'  , DATASET);
%descriptor.hks   = Get_Signature(evecs, evals, 'HKS'  , DATASET);
%descriptor.wks   = Get_Signature(evecs, evals, 'WKS'  , DATASET);
%descriptor.sihks = Get_Signature(evecs, evals, 'SIHKS', DATASET);
%descriptor.sgws  = Get_Signature(evecs, evals, 'SGWS' , DATASET);

%plotMesh0(vertices,faces,descriptor.gps(:,2));
plotMesh0(vertices,faces,descriptor.hks(:,2));
%plotMesh0(vertices,faces,descriptor.wks(:,2));
plotMesh0(vertices,faces,descriptor.sihks(:,1));
plotMesh0(vertices,faces,descriptor.sihks(:,2));
plotMesh0(vertices,faces,descriptor.sihks(:,3));
plotMesh0(vertices,faces,descriptor.sihks(:,4));
plotMesh0(vertices,faces,descriptor.sihks(:,5));
plotMesh0(vertices,faces,descriptor.sihks(:,6));
%plotMesh0(vertices,faces,descriptor.sgws(:,2));

save('myTest', 'descriptor')






% compute the specfic spectral descriptor
%desc = Get_Signature(evecs, evals,DescriptorType,DATASET);

% visualize the one dimension of the descriptor
%color = desc(:,6);
%plotMesh0(vertices,faces,color);

%stlwrite(FV,'meshWorking.stl')





%end