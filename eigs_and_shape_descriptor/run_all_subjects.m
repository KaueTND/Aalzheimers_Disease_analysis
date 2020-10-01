function run_all_subjects(path)%'../whichFiles.txt'
    fileID = fopen(path,'r');
    dirinfo = textscan(fileID,'%s','delimiter','\n');
    dirinfo = dirinfo{1,1};

    for K = 1 : length(dirinfo)
       thisdir = dirinfo{K};
       disp(thisdir);
       generate_eigs(thisdir,'/Volumes/CipacProcessing/Projects/RF_KaueAlzheimers/');

    end
end



% listing = dir(join('../brain_region_mat/'));
% %generate_eigs('128_S_0545','/Volumes/CipacProcessing/Projects/RF_KaueAlzheimers/');
% % 
%  for i=1:length(listing)
%     %if length(listing(i).name) == 10
%     %    disp(listing(i).name);
%         generate_eigs(listing(i).name,'/Volumes/CipacProcessing/Projects/RF_KaueAlzheimers/');
%     %end
%  end