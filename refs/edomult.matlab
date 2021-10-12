function C=edomult(~,C)
    
    %concentrações
    Ca=C(1);
    Cb=C(2);
    Ce=C(3);
    Cw=C(4);
    
    %eaquações diferenciais
    
    %parâmetros ajustáveis: B   MUDARÁ
    dCadt=-(B*Ccat*CTIres+Ccat*CTIacido*A)*exp(-Ead/(R*T))*(Ca*Cb-Ce*Cw/Keq);         
    dCbdt=-(B*Ccat*CTIres+Ccat*CTIacido*A)*exp(-Ead/(R*T))*(Ca*Cb-Ce*Cw/Keq);          
    dCedt=(B*Ccat*CTIres+Ccat*CTIacido*A)*exp(-Ead/(R*T))*(Ca*Cb-Ce*Cw/Keq);           
    dCwdt=(B*Ccat*CTIres+Ccat*CTIacido*A)*exp(-Ead/(R*T))*(Ca*Cb-Ce*Cw/Keq);          
    
    dCdt=[dCadt; dCbdt; dCedt; dCwdt]; %Matriz concentração (col) x Tempo (lin)
endfunction
