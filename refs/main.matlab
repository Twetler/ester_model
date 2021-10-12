 clear;

%número de intervalos para cada variável
passos=1;
%input('número de valores iterados para cada experimento')

%intervalos de iteração desejados para os valores dos parâmetros de ajuste.
liminfA=5.85e6;
limsupA=5.888e6;
%5.888e6

liminfB=3.1e3;
limsupB=3.150e3;
%3.150e3

%gráficos juntos (1) ou separados (2)?
graphmode=input('modo grafico 1 para junto e 2 para separado');

%Parâmetros de Reação
Ead=47341; %energia de ativação da reação direta em J/mol
Eai=50739;%energia de ativação da reação inversa em J/mol
R=8.31; %J/(mol*K) - constante de Boltzmann
V=0.35;%volume reacional
Vacido=0.35;%volume correspondente ao ácido
Keq=5.2;%constante de equilíbrio
Ka=1;
Kb=3.591; % (L/mol)
Kw= 15.748; % (L/mol)
Ke= 4.1209;
Da=1.16e-9; % (m²/s)
Db=1.5e-9; % (m²/s)
De=1.75e-10; % (m²/s)
Dw=1.54e-9; % (m²/s)
kca=0.0887; % (m/s)
kcb=0.1077; % (m/s)
kce=0.125; % (m/s)
kcw=0.0418; % (m/s)
Kpa=0.0246;
Kpb=0.0348;
Kpe=0.00636;
Kpw=0.035;
V2=77.4e-6; % m³
rho=0.9;

%estabelecento um contador para monitorar o número da iteração - não mexer
counter=1;

intB=linspace(liminfB,limsupB,passos);
intA=linspace(liminfA,limsupA,passos);

for testeB=1:length(intB)      %
B=intB(testeB);
    for testeA=1:length(intA)
    A=intA(testeA);

%dados experimentais das reações com álcool octílico
texp=[5, 15,30,45,60,75,90,105,120];
CESEG1=[0.049,0.049,0.060,0.071,0.092,0.092,0.114,0.146,0.184];
CESPEG1= [0.052,0.058,0.063,0.069,0.079,0.090,0.134,0.128,0.144];
CAMB1=[-0.009,0.109,0.125,0.141,0.163,0.184,0.206,0.216,0.259];
TMPTA=[0.020,0.041,0.052,0.079,0.095,0.095,0.106,0.138,0.181];
%ESSA%
S9=[0.039,0.071,0.119,0.173,0.216,0.259,0.280,0.334,0.323];%CONVERSOES
%^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
S9_70_1=[-0.02949421, 0.031202078, 0.107072438, 0.19811687, 0.266400194, 0.342270554, 0.433314986, 0.471250166, 0.524359418; 273.15+70, 1.087/1000, 1, 3.1 0 0 0 0 0];
S9_80_1=[0.086021422, 0.207983936, 0.329946451, 0.421418338, 0.482399595, 0.520512881, 0.581494138, 0.596739453, 0.650098053; 273.15+80, 1.087/1000, 1, 3.1 0 0 0 0 0];
S9_70_3=[0.170420738, 0.299565494, 0.436307, 0.527468004, 0.580645256, 0.641419259, 0.679403011, 0.724983513, 0.755370514; 273.15+70, 1.087/1000, 3, 3.1 0 0 0 0 0];
S9_80_3=[0.247596325, 0.422419766, 0.559238111, 0.658051361, 0.703657476, 0.741662572, 0.772066648, 0.787268687, 0.794869706; 273.15+80, 1.087/1000, 3, 3.1 0 0 0 0 0];
ASP_70_0062=[0.029, 0.145, 0.183, 0.203, 0.261, 0.261, 0.338, 0.377, 0.377; 273.15+70 1/98.079 0.062/V 0 0 0 0 0 0];
ASP_70_0094=[0.255, 0.305, 0.338, 0.371, 0.438, 0.438, 0.488, 0.504, 0.571; 273.15+70 1/98.079 0.094/V 0 0 0 0 0 0];
ASP_80_0033=[0.029, 0.029, 0.106, 0.183, 0.183, 0.222, 0.241, 0.261, 0.319; 273.15+80 1/98.079 0.033/V 0 0 0 0 0 0];
ASP_80_1100=[0.338, 0.338, 0.571, 0.687, 0.784, 0.803, 0.803, 0.880, 0.880; 273.15+80 1/98.079 1.1/V 0 0 0 0 0 0];
Aiso7003=[0.0952034, 0.2456301, 0.4038225, 0.5114513, 0.5874395, 0.6425014, 0.6831558, 0.7135902, 0.7366104];

%comando para inserir os conjuntos de dados desejados (inserir um por linha).
conjuntosdedados=[S9_70_1;S9_80_1;S9_70_3;S9_80_3;ASP_70_0062;ASP_80_0033;ASP_70_0094;ASP_80_1100];

%-----loop que realiza a simulação para cada conjunto de dados colocado no vetor 'conjuntosdedados'
for jdados = 1:((size(conjuntosdedados(1)))/2)

%definindo o vetor de resultados experimentais a partir da linha correspondente
dexp=conjuntosdedados((1 + (jdados-1)*2),:);

%filtro para valores nulos
%logind=dexp(:)==0
%dexp(logind)=[]

%temperatura correspondente ao conjunto de dados atual em K
%posição (2,1) na matriz de dados
T=conjuntosdedados((2 + (jdados-1)*2),1);

%cálculo da concentração de ácido para o caso da catálise homogênea em mol/g
%posição (2,2) na matriz de dados
CTIacido=conjuntosdedados((2 + (jdados-1)*2),2);

%Concentração de catalisador para o caso da catálise heterogênea em g/L
%Posição (2,3) na matriz de dados
Ccat=conjuntosdedados((2 + (jdados-1)*2),3);

%Capacidade de troca iônica referente ao catalisador em mol/g
%Posição (2,4) na matriz de dados
CTIres=conjuntosdedados((2 + (jdados-1)*2),4);


%-----Condições iniciais
%Concentrações em mol/L
Ca0=2.703/V; 
Cb0=1.802/V;
Ce0=0/V;
Cw0=1e-9/V;

%ponto de partida no tempo
t0=0;

deltat=0:0.1:120; %tempo em minutos
C0=[Ca0; Cb0; Ce0; Cw0]; %vetor das concentrações iniciais

% função do sistema de EDOs para catálise heterogênea
%-----------------------NONLIN SYSTEM GOES HEEEEEEEERE-----------------------------


%----------------------------NONLIN SYS ENDS HEEEEEEEEEEEEEERE---------------------
C= ode45(edomult,[t0 120],C0)';
%Resultados
Ca= C(:,1); 
Cb= C(:,2);
Ce= C(:,3);
Cw= C(:,4);

%transformando concentrações em conversão (observar reagente limitante)
for jCb = 1:length(Cb)
    Xb(jCb)=(Cb0-Cb(jCb))/(Cb0);
end

%obtendo valores da conversão na simulação correspondentes aos tempos experimentais
for jdeltat=1:length(deltat)
    for jtexp=1:length(texp)
        if deltat(jdeltat)==texp(jtexp)
         Xbmodel(jtexp)=Xb(jdeltat);
        end
     end
end

%-----gráficos de comparação dos experimentos com o modelo

%desenhando eixo horizontal
for jhaxis=1:length(deltat)
haxis(jhaxis)=0;
end

if graphmode==2 

%gráficos de conversão para cada experimento em comparação com o modelo
if dexp==conjuntosdedados(1,:) 
scf(1)
h = gca(); 
h.data_bounds = [0, 0 ; 120, 1];
h.font_size=5;
%title('70 °C - 1% de catalisador - catálise heterogênea','fontsize',5)
xlabel('tempo (min)','fontsize',5)
ylabel('conversão','fontsize',5)
plot(deltat,Xb,'-',texp,dexp,'or')%gráfico da simulação e experimental
hl=legend(['simulação';'dados experimentais']);
scf(2)
h = gca(); 
h.data_bounds = [0, -0.4 ; 120, 0.4];
h.font_size=5;
%title('70 °C - 1% de catalisador - catálise heterogênea','fontsize',5)
xlabel('tempo (min)','fontsize',5)
ylabel('resíduo','fontsize',5)
plot(texp,dexp-Xbmodel','or',deltat,haxis,'r') %gráfico de resíduos
elseif dexp==conjuntosdedados(3,:) 
scf(3)
h = gca(); 
h.data_bounds = [0, 0 ; 120, 1];
h.font_size=5;
%title('80 °C - 1% de catalisador - catálise heterogênea','fontsize',5)
xlabel('tempo (min)','fontsize',5)
ylabel('conversão','fontsize',5)
plot(deltat,Xb,'-',texp,dexp,'or') %gráfico da simulação e experimental
hl=legend(['simulação';'dados experimentais']);
scf(4)
h = gca(); 
h.data_bounds = [0, -0.4 ; 120, 0.4];
h.font_size=5;
%title('80 °C - 1% de catalisador - catálise heterogênea','fontsize',5)
xlabel('tempo (min)','fontsize',5)
ylabel('resíduo','fontsize',5)
plot(texp,dexp-Xbmodel','or',deltat,haxis,'r') %gráfico de resíduos
elseif dexp==conjuntosdedados(5,:) 
scf(5)
h = gca(); 
h.data_bounds = [0, 0 ; 120, 1];
h.font_size=5;
%title('70 °C - 3% de catalisador - catálise heterogênea','fontsize',5)
xlabel('tempo (min)','fontsize',5)
ylabel('conversão','fontsize',5)
plot(deltat,Xb,'-',texp,dexp,'or')%gráfico da simulação e experimental
hl=legend(['simulação';'dados experimentais']);
scf(6)
h = gca(); 
h.data_bounds = [0, -0.4 ; 120, 0.4];
h.font_size=5
%title('70 °C - 3% de catalisador - catálise heterogênea','fontsize',5)
xlabel('tempo (min)','fontsize',5)
ylabel('resíduo','fontsize',5)
plot(texp,dexp-Xbmodel','or',deltat,haxis,'r') %gráfico de resíduos
elseif dexp==conjuntosdedados(7,:) 
scf(7)
h = gca(); 
h.data_bounds = [0, 0 ; 120, 1];
h.font_size=5;
%title('80 °C - 3% de catalisador - catálise heterogênea','fontsize',5)
xlabel('tempo (min)','fontsize',5)
ylabel('conversão','fontsize',5)
plot(deltat,Xb,'-',texp,dexp,'or')%gráfico da simulação e experimental
h2=legend(['simulação';'dados experimentais'],4);
scf(8)
h = gca(); 
h.data_bounds = [0, -0.4 ; 120, 0.4];
h.font_size=5;
%title('80 °C - 3% de catalisador - catálise heterogênea','fontsize',5)
xlabel('tempo (min)','fontsize',5)
ylabel('resíduo','fontsize',5)
plot(texp,dexp-Xbmodel','or',deltat,haxis,'r') %gráfico de resíduos
elseif dexp==conjuntosdedados(9,:) 
scf(9)
h = gca(); 
h.data_bounds = [0, 0 ; 120, 1];
h.font_size=5;
%title('70 °C - 0,062g de ácido sulfúrico - catálise homogênea','fontsize',5)
xlabel('tempo (min)','fontsize',5)
ylabel('conversão','fontsize',5)
plot(deltat,Xb,'-',texp,dexp,'or')%gráfico da simulação e experimental
hl=legend(['simulação';'dados experimentais']);
scf(10)
h = gca(); 
h.data_bounds = [0, -0.4 ; 120, 0.4];
h.font_size=5;
%title('70 °C - 0,062g de ácido sulfúrico - catálise homogênea','fontsize',5)
xlabel('tempo (min)','fontsize',5)
ylabel('resíduo','fontsize',5)
plot(texp,dexp-Xbmodel','or',deltat,haxis,'r') %gráfico de resíduos
elseif dexp==conjuntosdedados(11,:) 
scf(11)
h = gca(); 
h.data_bounds = [0, 0 ; 120, 1];
h.font_size=5;
%title('80 °C - 0,033g de ácido sulfúrico - catálise homogênea','fontsize',5)
xlabel('tempo (min)','fontsize',5)
ylabel('conversão','fontsize',5)
plot(deltat,Xb,'-',texp,dexp,'or')%gráfico da simulação e experimental
hl=legend(['simulação';'dados experimentais']);
scf(12)
h = gca(); 
h.data_bounds = [0, -0.4 ; 120, 0.4];
h.font_size=5;
%title('80 °C - 0,033g de ácido sulfúrico - catálise homogênea','fontsize',5)
xlabel('tempo (min)','fontsize',5)
ylabel('resíduo','fontsize',5)
plot(texp,dexp-Xbmodel','or',deltat,haxis,'r') %gráfico de resíduos
elseif dexp==conjuntosdedados(13,:) 
scf(13)
h = gca(); 
h.data_bounds = [0, 0 ; 120, 1];
h.font_size=5;
%title('70 °C - 0,094g de ácido sulfúrico - catálise homogênea','fontsize',5)
xlabel('tempo (min)','fontsize',5)
ylabel('conversão','fontsize',5)
plot(deltat,Xb,'-',texp,dexp,'or')%gráfico da simulação e experimental
hl=legend(['simulação';'dados experimentais']);
scf(14)
h = gca(); 
h.data_bounds = [0, -0.4 ; 120, 0.4];
h.font_size=5;
%title('70 °C - 0,094g de ácido sulfúrico - catálise homogênea','fontsize',5)
xlabel('tempo (min)','fontsize',5)
ylabel('resíduo','fontsize',5)
plot(texp,dexp-Xbmodel','or',deltat,haxis,'r') %gráfico de resíduos
elseif dexp==conjuntosdedados(15,:) 
scf(15)
h = gca(); 
h.data_bounds = [0, 0 ; 120, 1];
h.font_size=5;
%title('80 °C - 1,1g de ácido sulfúrico - catálise homogênea','fontsize',5)
xlabel('tempo (min)','fontsize',5);
ylabel('conversão','fontsize',5);
plot(deltat,Xb,'-',texp,dexp,'or');%gráfico da simulação e experimental
hl=legend(['simulação';'dados experimentais'],4);
scf(16);
h = gca(); 
h.data_bounds = [0, -0.4 ; 120, 0.4];
h.font_size=5;
%title('80 °C - 1,1g de ácido sulfúrico - catálise homogênea','fontsize',5)
xlabel('tempo (min)','fontsize',5);
ylabel('resíduo','fontsize',5);
plot(texp,dexp-Xbmodel','or',deltat,haxis,'r'); %gráfico de resíduos
end 

elseif graphmode==1  %caso em que se deseja gráficos separados

if dexp==conjuntosdedados(1,:)
scf(1);
subplot(4,2,1);
xlabel('70 - 1% heterogênea');
plot(deltat,Xb,'-',texp,dexp,'or');%gráfico da simulação e experimental
scf(2);
subplot(4,2,1);
plot(texp,dexp-Xbmodel','or',deltat,haxis,'r'); %gráfico de resíduos
elseif dexp==conjuntosdedados(3,:) 
scf(1);
subplot(4,2,2);
xlabel('80 - 1% heterogênea');
plot(deltat,Xb,'-',texp,dexp,'or'); %gráfico da simulação e experimental
scf(2);
subplot(4,2,2);
plot(texp,dexp-Xbmodel','or',deltat,haxis,'r'); %gráfico de resíduos
elseif dexp==conjuntosdedados(5,:) 
scf(1);
subplot(4,2,3);
xlabel('70 - 3% heterogênea');
plot(deltat,Xb,'-',texp,dexp,'or');%gráfico da simulação e experimental
scf(2);
subplot(4,2,3);
plot(texp,dexp-Xbmodel','or',deltat,haxis,'r'); %gráfico de resíduos
elseif dexp==conjuntosdedados(7,:) 
scf(1);
subplot(4,2,4);
xlabel('80 - 3% heterogênea')
plot(deltat,Xb,'-',texp,dexp,'or')%gráfico da simulação e experimental
scf(2)
subplot(4,2,4)
plot(texp,dexp-Xbmodel','or',deltat,haxis,'r') %gráfico de resíduos
elseif dexp==conjuntosdedados(9,:) 
scf(1)
subplot(4,2,5)
xlabel('70 - 0,062g homogênea')
plot(deltat,Xb,'-',texp,dexp,'or')%gráfico da simulação e experimental
scf(2)
subplot(4,2,5)
plot(texp,dexp-Xbmodel','or',deltat,haxis,'r') %gráfico de resíduos
elseif dexp==conjuntosdedados(11,:) 
scf(1)
subplot(4,2,6)
xlabel('80 - 0,0033g homogênea')
plot(deltat,Xb,'-',texp,dexp,'or')%gráfico da simulação e experimental
scf(2)
subplot(4,2,6)
plot(texp,dexp-Xbmodel','or',deltat,haxis,'r') %gráfico de resíduos
elseif dexp==conjuntosdedados(13,:) 
scf(1)
subplot(4,2,7)
xlabel('70 - 0,094g homogênea')
plot(deltat,Xb,'-',texp,dexp,'or')%gráfico da simulação e experimental
scf(2)
subplot(4,2,7)
plot(texp,dexp-Xbmodel','or',deltat,haxis,'r') %gráfico de resíduos
elseif dexp==conjuntosdedados(15,:) 
scf(1)
subplot(4,2,8)
xlabel('80 - 1,1g homogênea')
plot(deltat,Xb,'-',texp,dexp,'or')%gráfico da simulação e experimental
scf(2)
subplot(4,2,8)
plot(texp,dexp-Xbmodel','or',deltat,haxis,'r') %gráfico de resíduos
end 
hl=legend(['simulação';'dados experimentais']);


end
%-----cálculo da soma quadrática dos resíduos para a presente iteração do presente experimento



%calculando os resíduos para a presente iteração do presente experimento
res=abs(Xbmodel'-dexp);%calculando o resíduo para cada ponto experimental
%cálculo de resíduo percentual médio
respm=100*mean(res/dexp);
%criando uma matriz com os resíduos de cada iteração de cada experimento
respmmatrix=respm(counter,jdados);
resSQ=(Xbmodel'-dexp).^2; %calculando o quadrado do resíduo para cada ponto experimental
%calculando a somatóriados resíduos para a iteração
resSQsum=sum(resSQ);
%criando uma matriz com a soma quadrática dos resíduos de cada iteração de cada experimento
resSQmatrix(counter,jdados)=resSQsum;

%Criando uma matriz com o quadrado dos resíduos de cada iteração de cada experimento

%-----fim das iterações
end%fim do loop dos conjuntos de dados

%criando matrizes com todos os valores utilizados dos parâmetros de ajuste
matrizB(counter)=B;
matrizA(counter)=A;

counter=counter+1;%somando 1 ao contador após obtidos os valores de todos os conjuntos experimentais

end%fim do loop de resoluções para uma das variáveis
end%fim do loop de resoluções para uma das variáveis


%construindo uma matriz coluna com as médias totais dos erros percentuais dos experimentos para cada iteração

for j=1:(size(respmmatrix(1)))
respmtotal(j)=mean(respmmatrix(j,:));
end

%construindo uma matriz coluna com a soma dos quadrados dos resíduos dos experimentos para cada iteração
for j=1:(size(resSQmatrix(1)))
resSQtotal(j)=sum(resSQmatrix(j,:));
end


%for jsqresmatrix=1:(size(sqresmatrix)(1))
%    resfinal(jsqresmatrix,1)=sum(sqresmatrix(jsqresmatrix,:))
%end

for jN=1:(size(respmmatrix(1)))
    matrizindice(jN,1)=jN;
end

%-----criando a matriz tabela com os valores da soma quadrática dos resíduos e valores ajustados correspondentes
vetordemo=[matrizindice, respmtotal, resSQtotal, matrizA, matrizB];

%-----expondo as tabelas de dados
disp('melhor ajuste encontrado pelo método dos mínimos quadrados')
for j=1:size(vetordemo(1))
    if vetordemo(j,3)==min(vetordemo(:,3));
    disp(vetordemo(j,:));
    end
end
disp('erro médio do modelo para cada experimento');
disp(respmmatrix');
