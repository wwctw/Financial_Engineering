%% 輸入引數
principal = input('請輸入本金(元): ');
year = input('請輸入期數(年): ');
rate = input('請輸入年利率(%): ');

%% 計算每個月應償還本金及利息
pr_month = ceil( principal/(12*year) ); %每月攤還本金無條件進位
pr_last_month = principal - (12*year-1)*pr_month; %最後一期要特別處理
principal_left = principal; %原始本金
sum_interest = 0; %利息總和

%第1個月本金利息累計需從0開始，需特別處理
interest_month(1) = round( principal_left*(0.01*rate/12) ); %利息四捨五入
principal_left = principal_left - pr_month;
sum_interest = sum_interest + interest_month(1);
cum_pr_int(1) = pr_month + interest_month(1);

%第2個月到最後一個月
for k = 2:(12*year)
    interest_month(k) = round( principal_left*(0.01*rate/12) );
    principal_left = principal_left - pr_month;
    sum_interest = sum_interest + interest_month(k);
    cum_pr_int(k) = cum_pr_int(k-1) + pr_month + interest_month(k);
end
%最後一個月償還的本金不是平均每月攤還本金，需特別處理
cum_pr_int(k) = cum_pr_int(k-1) + pr_last_month + interest_month(k);
principal_left = principal_left + pr_month - pr_last_month; %確認本金歸零

%% 輸出結果
fprintf('\n  本金             %14.0f 元\n',principal);
fprintf('  期數(年)         %14.0f\n',year);
fprintf('  年利率           %14.0f %%\n',rate);
fprintf('  每月攤還本金     %14.0f 元\n',pr_month);
fprintf('  每月攤還利息          請參考下表\n');
fprintf('  全部利息         %14.0f 元\n\n',sum_interest);
fprintf('               本金(元)         利息(元)    本金利息累計(元)\n')
for k = 1:(12*year-1)
    fprintf('  第%03.0f期  %14.0f   %14.0f   %14.0f\n',k,pr_month...
        ,interest_month(k),cum_pr_int(k));
end
fprintf('  第%03.0f期  %14.0f   %14.0f   %14.0f\n',12*year,pr_last_month...
    ,interest_month(12*year),cum_pr_int(12*year));

