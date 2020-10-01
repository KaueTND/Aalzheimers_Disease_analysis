%insert all-region reading obtained by analyzing all the other regions.

allregions = load('../all_regions_nodes.mat');
allregionssimilarity = cell(length(dirinfo),1);
for i = 1 : length(allregions.regions)
    disp(allregions.regions(i))
end

fileID = fopen('../procedure_mat.txt','r');
d = textscan(fileID,'%s','delimiter','\n');
d = d{1,1}

region = 4;
regionFileExtension = strcat('*x',num2str(region),'.mat');

dirDescriptor = '../descriptor/';
dirinfo = dir(dirDescriptor);
dirinfo(~[dirinfo.isdir]) = [];

subdirinfo = cell(length(dirinfo),1);% remove . and .. dirs
pathToStructure = cell(length(dirinfo)-2,1);

for K = 3 : length(dirinfo)
  thisdir = d{K-2};
  searchDir = strcat(dirDescriptor,thisdir);
  subdirinfo{K-2} = (dir(fullfile(searchDir, regionFileExtension)));
  pathToStructure{K-2} = strcat(subdirinfo{K-2}.folder,'/',subdirinfo{K-2}.name);
end

for K = 1 : length(pathToStructure)
  disp(pathToStructure{K});
end

%grouping to identify the visual vocabulary
disp('Grouping for kMeans');
sizeSihks = zeros(length(pathToStructure),1);

final_stack_region = [];
for i = 1: length(pathToStructure)
    descriptor = load(pathToStructure{i});
    zscoredsihks = zscore(descriptor.descriptor.sihks);
    final_stack_region = vertcat(final_stack_region,zscoredsihks);
    %disp(length(descriptor.descriptor.sihks));
    sizeSihks(i) = length(descriptor.descriptor.sihks);
end

disp('Applying K-means');

k=100;

[idx,C] = kmeans(final_stack_region,k);

%splitting to return the vectors to their own meshes
sihksResults = cell(length(pathToStructure),1);
accumulator=1;

sihksResults = {};

disp('Splitting vectors after kMeans');

for i = 1: length(pathToStructure)
    %final_stack_region = vertcat(final_stack_region,descriptor.descriptor.sihks);
    sihksResults{i} = (idx(accumulator:sizeSihks(i,1)+accumulator-1));
    accumulator = accumulator + sizeSihks(i,1);
end

regionFileExtension = strcat('*x',num2str(region),'.stl');
dirDescriptor = '../brain_region_mat/';
dirinfo = dir(dirDescriptor);
dirinfo(~[dirinfo.isdir]) = [];

subdirinfo = cell(length(dirinfo)-2,1);% remove . and .. dirs
%pathToStructure = cell(length(dirinfo)-2,1);
histograms = cell(length(dirinfo)-2,1);

disp('Generating Histograms');

for K = 3 : length(dirinfo)
  thisdir = d{K-2}; 
  searchDir = strcat(dirDescriptor,thisdir);
  subdirinfo{K-2} = (dir(fullfile(searchDir, regionFileExtension)));
  
  FV = stlread(strcat(dirinfo(K-2).folder,'/',thisdir,'/',thisdir,'x4.stl'));

  vertices = FV.Points;
  faces    = FV.ConnectivityList;
  %plotMesh0(vertices,faces,sihksResults{K-2});
  H = histogram(sihksResults{K-2},100);
  histograms{K-2} = H.Values;
end



similaritymatrix = zeros(length(dirinfo)-2,length(dirinfo)-2);

for Ki = 3 : length(dirinfo)
    for Kj = 3 : length(dirinfo)
        coef = corrcoef(histograms{Ki-2},histograms{Kj-2});
        similaritymatrix(Ki-2,Kj-2) = coef(1,2);
    end
end

OO = mat2gray(similaritymatrix);

imshow(OO);








