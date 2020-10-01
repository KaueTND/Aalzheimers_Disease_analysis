function newONE_CHANGE(interval)%'../procedure_mat.txt'

disp(interval);
%insert all-region reading obtained by analyzing all the other regions.
filename = '../final_test_2_final.txt';
allregions = load('../all_regions_nodes.mat');
%regions = allregions.allregions.regions;

allregionssimilarity = cell(length(allregions.regions),1);
fileID = fopen(filename,'r');
dirinfo = textscan(fileID,'%s','delimiter','\n');
dirinfo = dirinfo{1,1};
n = 3;
Cbmat = reshape(allregions.regions, [], n);
interval = str2num(interval)
allregions.regions = Cbmat(:,interval);



for regionID = 1 : length(allregions.regions)
% region = 4;
% if region == 4
    %disp(allregions.regions(regionID))
    try
    region = allregions.regions(regionID);
    %region=3;
    disp(region);
    
    regionFileExtensionMAT = strcat('*x',num2str(region),'.mat');
    regionFileExtensionSTL = strcat('*x',num2str(region),'.stl');
    
    %regionFileExtension = strcat('*x',num2str(allregions.regions(regionID)),'.mat');
    
    dirDescriptor = '../descriptor/';
    dirBrain = '../brain_region_mat/';
    
    %dirinfo = dir(dirDescriptor);
    %dirinfo(~[dirinfo.isdir]) = [];

    subdirinfo = cell(length(dirinfo),1);% remove . and .. dirs
    pathToStructure = cell(length(dirinfo),1);

    for K = 1 : length(dirinfo)
      thisdir = dirinfo{K};
      searchDir = strcat(dirDescriptor,thisdir);
      subdirinfo{K} = (dir(fullfile(searchDir, regionFileExtensionMAT)));
      pathToStructure{K} = strcat(subdirinfo{K}.folder,'/',subdirinfo{K}.name);
    end


    workIDs = {};
    followID = 1;
    for K = 1 : length(pathToStructure)
      if (strcmp(pathToStructure{K},'/')==0)
          %disp(pathToStructure{K});
          workIDs{followID} = K;
          followID = followID+1;
      end
    end
% % 
    %grouping to identify the visual vocabulary
    sizeSihks = zeros(length(pathToStructure),1);

    final_stack_region = [];
    for i = 1: length(workIDs)
        value = workIDs{i};
        descriptor = load(pathToStructure{value});
        zscoredsihks = (descriptor.descriptor.sihks);
        final_stack_region = vertcat(final_stack_region,zscoredsihks);
        %disp(length(descriptor.descriptor.sihks));
        sizeSihks(value) = length(descriptor.descriptor.sihks);
    end
% 
    disp('Applying K-means');

    k=100;

    [idx,C] = kmeans(final_stack_region,k);% 
%     %splitting to return the vectors to their own meshes
    sihksResults = cell(length(pathToStructure),1);
    accumulator=1;

    sihksResults = {};

    disp('Splitting vectors after kMeans');
% 
    for i = 1: length(workIDs)
        value = workIDs{i};
        descriptor = load(pathToStructure{value});   
        %final_stack_region = vertcat(final_stack_region,descriptor.descriptor.sihks);
        sihksResults{i} = (idx(accumulator:sizeSihks(value,1)+accumulator-1));
        accumulator = accumulator + sizeSihks(value,1);
    end
% 
%     
 
    subdirinfo = cell(length(dirinfo),1);% remove . and .. dirs
    pathToStructure = cell(length(dirinfo),1);
    histograms = cell(length(dirinfo),1);

    disp('Generating Histograms');

    for i = 1: length(workIDs)
      value = workIDs{i};
      %thisdir = dirinfo{value}; 
      
      %searchDir = strcat(dirBrain,thisdir);
      %subdirinfo{value} = (dir(fullfile(searchDir, regionFileExtensionSTL)));
      
      %folderx = subdirinfo{value}(1);
      %disp(strcat(folderx.folder,'/',thisdir,'x',num2str(region),'.stl'));
      
      %for sake of viewing
      %FV = stlread(strcat(folderx.folder,'/',thisdir,'x',num2str(region),'.stl'));

      %vertices = FV.Points;
      %faces    = FV.ConnectivityList;
      %plotMesh0(vertices,faces,sihksResults{K});
      %end for sake of viewing
      
      H = histogram(sihksResults{i},k);
      histograms{value} = H.Values;
      histo = H.Values;
      
    end
 
      file = strcat('../histogram/simi_',num2str(region),'.mat');
      save(file,'histograms') 
 
     similaritymatrix = zeros(length(dirinfo),length(dirinfo));
 
     for Ki = 1 : length(workIDs)
         wKi = workIDs{Ki};
         for Kj = 1 : length(workIDs)
             wKj = workIDs{Kj};
             coef = corrcoef(histograms{wKi},histograms{wKj});
             similaritymatrix(wKi,wKj) = coef(1,2);
         end
     end
% 
     simi = mat2gray(abs(similaritymatrix));
     imshow(simi);
     file = strcat('../preliminary_results/simi_',num2str(region),'.mat');
     save(file,'simi')
     
     %allregionssimilarity{regionID} = OO;
    catch MExc
        message = strcat('Error in region',num2str(region),'. Check quantity of this regions per subjects.');
        disp(message);
    end
end
end 









