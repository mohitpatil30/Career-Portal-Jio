function checkboxlimit(checkgroup,limit) 
{
	var checkgroup = checkgroup,limit = limit;
	for (var i=0; i<checkgroup.length; i++)
	{
        	var checkedcount=0;
        	for (var i=0; i<checkgroup.length; i++)
            	checkedcount += (checkgroup[i].checked) ? 1 : 0;
        	if (checkedcount > limit)
        	{
            	this.checked = false;
            	return false;
        	}
        	else if(checkedcount <limit)
        	{
         		this.checked=false;
             	return false;
        	}
        	else
        	 	return true;
	}
}
function checkInput()
{
	var limit = 2;
	var validInput = checkboxlimit(document.getElementsByName("role_list"),limit);
	return validInput;
}