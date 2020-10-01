function generate_eigs(subject,pathToMainFolder)




    %alpha = 2;          % log scalespace basis
    %subject = '016_S_1326';

    DATASET = 'SHREC2011_Nonrigid';  % dataset to process. 'PARAMETERS_test.m' 'SHREC2011_Nonrigid'

    % set path for auxilary code
    addpath(genpath(fullfile('sgwt_toolbox')));  % spectral graph wavelets code
    %addpath(fullfile('meshcodes')); 

    
    if nargin == 1
        pathToMainFolder = '../'; 
    end
    listing = dir(join([pathToMainFolder,'brain_region_mat/',subject,'/',subject,'*stl']));


    %parfor i=1:length(listing)
    for i=1:length(listing)
        K = 30;
        FV = stlread(join([pathToMainFolder,'brain_region_mat/',subject,'/',listing(i).name],''));
        shape = struct();
        shape.X = FV.Points(:,1);
        shape.Y = FV.Points(:,2);
        shape.Z = FV.Points(:,3);
        shape.TRIV = FV.ConnectivityList;

        % compute cotan Laplacian
        [shape.W,shape.A] = mshlp_matrix(shape);
        shape.A = spdiags(shape.A,0,size(shape.A,1),size(shape.A,1));

        % compute eigenvectors/values
        try
            [shape.evecs,shape.evals] = eigs(shape.W,shape.A,K,'SM');
        catch MExc
		
		%disp(MExc.message);
	%	disp(listing(i).name);
        
		if startsWith(MExc.message,'First')  == 1
	   		continue;
  		else	   
	    		eigsNewK = split(MExc.message,'= ');
            		eigsNewK = split(eigsNewK{2},'.');
            		K = (str2num(eigsNewK{1}));
            		[shape.evecs,shape.evals] = eigs(shape.W,shape.A,K,'SM');
        	end
	end
        shape.evals = -diag(shape.evals);

        evecs = shape.evecs;
        evals = shape.evals;

        descriptor = struct();
        descriptor.gps   = Get_Signature(evecs, evals, 'GPS'  , DATASET);
        descriptor.hks   = Get_Signature(evecs, evals, 'HKS'  , DATASET);
        descriptor.wks   = Get_Signature(evecs, evals, 'WKS'  , DATASET);
        descriptor.sihks = Get_Signature(evecs, evals, 'SIHKS', DATASET);
        descriptor.sgws  = Get_Signature(evecs, evals, 'SGWS' , DATASET);

        fileName  = split(listing(i).name,'.');
        %fileName  = split(fileName{1},'x');
        %fileName  = strcat(fileName{1},'e',num2str(K),'x',fileName{2});
        finalPath = strcat(pathToMainFolder,'descriptor/',subject,'/',fileName{1},'.mat');
        %disp(finalPath)

        %save(finalPath,'evecs','evals')  
        parsave(finalPath,descriptor);
    end
end
