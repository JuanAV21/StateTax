<!DOCTYPE html>
<html><body>
<h1>Group 1</h1>
<p>


<p>{{param}}</p>
% par = param.split(',')
% state = par[0]
% amount = float(par[1])
<p>state = {{state}}</p>
<p>amount = {{amount}}</p>

% ok = True

% if state=='NY':
%    amountAftTax = amount * 1.05
% elif state=='MD':
%    amountAftTax = amount * 1.07
% else:
%    ok = False
     <p>I don't understand your state!</p>
     <p>please try NY or MD</P>
% end

% if ok:
   <p>amount before tax is {{amount}}</p>
   <p>amount after tax is {{amountAftTax}}</p>
% end

</body></html>