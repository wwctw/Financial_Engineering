%% ��J�޼�
principal = input('�п�J����(��): ');
year = input('�п�J����(�~): ');
rate = input('�п�J�~�Q�v(%): ');

%% �p��C�Ӥ����v�٥����ΧQ��
pr_month = ceil( principal/(12*year) ); %�C���u�٥����L����i��
pr_last_month = principal - (12*year-1)*pr_month; %�̫�@���n�S�O�B�z
principal_left = principal; %��l����
sum_interest = 0; %�Q���`�M

%��1�Ӥ륻���Q���֭p�ݱq0�}�l�A�ݯS�O�B�z
interest_month(1) = round( principal_left*(0.01*rate/12) ); %�Q���|�ˤ��J
principal_left = principal_left - pr_month;
sum_interest = sum_interest + interest_month(1);
cum_pr_int(1) = pr_month + interest_month(1);

%��2�Ӥ��̫�@�Ӥ�
for k = 2:(12*year)
    interest_month(k) = round( principal_left*(0.01*rate/12) );
    principal_left = principal_left - pr_month;
    sum_interest = sum_interest + interest_month(k);
    cum_pr_int(k) = cum_pr_int(k-1) + pr_month + interest_month(k);
end
%�̫�@�Ӥ��v�٪��������O�����C���u�٥����A�ݯS�O�B�z
cum_pr_int(k) = cum_pr_int(k-1) + pr_last_month + interest_month(k);
principal_left = principal_left + pr_month - pr_last_month; %�T�{�����k�s

%% ��X���G
fprintf('\n  ����             %14.0f ��\n',principal);
fprintf('  ����(�~)         %14.0f\n',year);
fprintf('  �~�Q�v           %14.0f %%\n',rate);
fprintf('  �C���u�٥���     %14.0f ��\n',pr_month);
fprintf('  �C���u�٧Q��          �аѦҤU��\n');
fprintf('  �����Q��         %14.0f ��\n\n',sum_interest);
fprintf('               ����(��)         �Q��(��)    �����Q���֭p(��)\n')
for k = 1:(12*year-1)
    fprintf('  ��%03.0f��  %14.0f   %14.0f   %14.0f\n',k,pr_month...
        ,interest_month(k),cum_pr_int(k));
end
fprintf('  ��%03.0f��  %14.0f   %14.0f   %14.0f\n',12*year,pr_last_month...
    ,interest_month(12*year),cum_pr_int(12*year));

