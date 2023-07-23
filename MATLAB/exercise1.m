clear all, close all
T = 1; ts = 0.01; % time horizon and discretization time
t = 0:ts:T; % time vector
phi = 0;
u = sin(2*pi*t + phi); % signal
figure, hold on, stem(t,u,"k")
title("Signal"), xlabel("time, t"), ylabel("u(t)")