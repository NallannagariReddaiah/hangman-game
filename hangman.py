#include<stdio.h>
#include<windows.h>
#include <unistd.h>
#include<time.h>
struct costomer{
	char name[10];
	char phone[15];
 	int tranition;
	int totalamt;
	int id;
	int password;
	int n;
};
void one(struct costomer[],int,int);
void two(struct costomer[],int,int);
void three(struct costomer[],int,int);
void four(struct costomer[],int,int);
void five(struct costomer[],int,int);
void printcostomer(struct costomer[],int );
int security(struct costomer[],int,int);
int block(struct costomer[],int,int);
void printfile(struct costomer[],int);
void check(struct costomer[],int,int,int);
void bank();
int main(){
	int x,n,i,j=0,q,mp,mpp,m=0;
	struct costomer o[10];
	FILE *p;
	p=fopen("myfile.txt","r");
	fscanf(p,"%d",&n);
	fscanf(p,"%d",&mp);
	for(i=2;i<n;i++){ 
	fscanf(p,"%d%d%s%d%s",&o[i].id,&o[i].password,o[i].phone,&o[i].totalamt,o[i].name);
}
	fclose(p);
	int a;
	char id[10];
	bank();
	printf("ENTER ID:");
	scanf("%s",id);
	printf("ENTER PASSWORD:");
	scanf("%d",&a);
if(a==mp){
	system("cls");bank();
	printf("LOGIN SUCESSFUL\n");
	sleep(2);
	system("cls");
	bank();
while(1){
	printf("1 TO GENARETION OF PIN\n");
	printf("2 TO BLOCK ATM CARD\n");
	printf("3 TO DEPOSIT AMOUNT\n");
	printf("4 TO DEBIT AMOUNT\n");
	printf("5 TO CHECK YOUR BANK BALENCE\n");
	printf("6 TO AXCESS AN BANK EMPLOYEE\n");
	printf("ENTER NUMBER");
	scanf("%d",&q);
	if(q==1){
	one(o,n,m);
	printf("THANK YOU\n");
	sleep(2);
	system("cls");bank();
	continue;
	}
	else if(q==2){
	two(o,n,m);
	printf("THANK YOU\n");
	sleep(2);
	system("cls");bank();
	continue;
	}
	else if(q==3){
	three(o,n,m);
	printf("THANK YOU\n");
	sleep(2);
	system("cls");bank();
	continue;
	}
	else if(q==4){
	four(o,n,m);
	printf("THANK YOU\n");
	sleep(2);
	system("cls");bank();
	continue;
	}
	else if(q==5){
	five(o,n,m);
	printf("THANK YOU\n");
	sleep(2);
	system("cls");bank();
	continue;
	}
	else{
		system("cls");
		bank();
		printf("ENTER 1 FOR FILL MONEY IN ATM MICHINE\n");
		printf("ENTER 2 FOR OFF THIS MICHINE");
		scanf("%d",&x);
		if(x==1){
				printf("ENTER YOUR PASSWORD");
				scanf("%d",&mpp);
				system("cls");
				bank();
			if (mp==mpp){
				system("cls");
				bank();
				printf("MICHINE IS OPPENED FILL THE AMMOUNT\a");
				sleep(2);
				system("cls");
				bank();
				continue;
				}
			else{
				sleep(2);
				system("cls");
				bank();
				continue;
				}	
		}
		else if(x==2){
				printf("ENTER YOUR PASSWORD");
				scanf("%d",&mpp);
				system("cls");
				bank();
			if (mp==mpp){
				system("cls");
				bank();
				printf("LOGGED OUT SUCESSFULLY");
				sleep(2);
				system("cls");
				bank();
				break;
				}
			else{
				sleep(2);
				system("cls");
				bank();
				continue;
				}	
			}
	}	
}
}
else {
	printf("INVALID ID OR PASSWORD");
}
return 0;
}
void printcostomer(struct costomer o[],int i){
	printf("%d%d%s%d%s",o[i].id,o[i].password,o[i].phone,o[i].totalamt,o[i].name);
}
void one(struct costomer o[],int n,int m){
	system("cls");bank();
	int i,j,k,l;
	i=security(o,n,m);
	if(i==0){
		printf("YOUR ACCOUNT HAS BEEN BLOCKED \n");
		printf("PLEASE CONTACT XYZ BANK FOR DETAILS\n");
		sleep(1);
	}
	else if(i==1){
		printf("ENTER 1 FOR HOME\n");
		printf("ENTER 2 FOR CONTINUE\n");
		scanf("%d",&l);
		if(l==1)
		return ;
		else
		one(o,n,m);
	}
	else{
		printf("ENTER YOUR NEW FOUR DIGIT PASSWORD:");
		scanf("%d",&k);
		printf("ENTER THE FOUR DIGIT PASSWORD FOR CONFORMATION:");
		scanf("%d",&j);
		if(k==j){
			o[i].password=k;
			printfile(o,n);
			printf("PROCESSING......");
			sleep(2);
			system("cls");bank();
			printf("PASSWORD CREATED SUCESSFULLY\n");
		}
		else{
		printf("TWO PASSWORDS ARE DIFFERENT \nPLEASE TRY AGAIN\n");	
		one(o,n,m);	
		}
	}

}
void two(struct costomer o[],int n,int m){
	system("cls");bank();
	int i,l;
	i=security(o,n,m);
	if(i==0){
		printf("YOUR ACCOUNT HAS BEEN BLOCKED \n");
		printf("PLEASE CONTACT XYZ BANK FOR DETAILS\n");
		sleep(1);
	}
	else if(i==1){
		printf("ENTER 1 FOR HOME\n");
		printf("ENTER 2 FOR CONTINUE\n");
		scanf("%d",&l);
		if(l==1)
		return ;
		else
		one(o,n,m);
	}
	else{

	block(o,i,n);
	printfile(o,n);
	}
	}
void three(struct costomer o[],int n,int m){
	system("cls");bank();
	int i,z,l;
	i=security(o,n,m);
	if(i==0){
		printf("YOUR ACCOUNT HAS BEEN BLOCKED \n");
		printf("PLEASE CONTACT XYZ BANK FOR DETAILS\n");
		sleep(1);
	}
	else if(i==1){
		printf("ENTER 1 FOR HOME\n");
		printf("ENTER 2 FOR CONTINUE\n");
		scanf("%d",&l);
		if(l==1)
		return ;
		else
		one(o,n,m);
	}
	else{	
		m=0;
		printf("ENTER THE AMOUNT:");
		scanf("%d",&z);
		o[i].totalamt+=z;
		printf("TRANSITION COMPLETED\n\a");
		printf("CHECK YOUR BALENCE\n");
		printfile(o,n);
		}
}
void four(struct costomer o[],int n,int m){
	system("cls");bank();
	int i,z,l;
	i=security(o,n,m);
	if(i==0){
		printf("YOUR ACCOUNT HAS BEEN BLOCKED \n");
		printf("PLEASE CONTACT XYZ BANK FOR DETAILS\n");
		sleep(1);
	}
	else if(i==1){
		printf("ENTER 1 FOR HOME\n");
		printf("ENTER 2 FOR CONTINUE\n");
		scanf("%d",&l);
		if(l==1)
		return ;
		else
		one(o,n,m);
	}
	else{
		m=0;
		printf("ENTER THE AMOUNT:");
		scanf("%d",&z);
		if(z<o[i].totalamt){
				o[i].totalamt-=z;
				printf("TRANSITION COMPLETED \nCOLLECT THE AMMOUNT\a\n");
				printf("CHECK THE BALENCE\n");
				printfile(o,n);
			}
		else{
			printf("YOU HAVE INSUFFFICENT BALENCE\n");
			return;
		}
		
	}
	}
void five(struct costomer o[],int n,int m){
	system("cls");bank();
	int i,l;
	i=security(o,n,m);
	if(i==0){
		printf("YOUR ACCOUNT HAS BEEN BLOCKED \n");
		printf("PLEASE CONTACT XYZ BANK FOR DETAILS\n");
		sleep(1);
	}
	else if(i==1){
		printf("ENTER 1 FOR HOME\n");
		printf("ENTER 2 FOR CONTINUE\n");
		scanf("%d",&l);
		if(l==1)
		return ;
		else
		one(o,n,m);
	}
	else
	{
		printf("YOUR ACCOUNT BALLENCE:%d\n",o[i].totalamt);
	}
	}
int security(struct costomer o[],int n,int m){
	system("cls");bank();
	int i,x,y,z;
	check(o,m,i,n);
	printf("ENTER YOUR ACCOUNT NUMBER:");
	scanf("%d",&x);
	for(i=2;i<n;i++) {
		if(o[i].id==x){
			printf("ENTER YOUR PASSWORD:");
			scanf("%d",&y);
			if(y==o[i].password){
				return i;
				}
				else if(o[i].password==0){
					return 0;	
					}
				else{
					printf("INCORRECT PASSWORD PLEASE TRY AGAIN....\n");
					m=m+1;
					sleep(2);
					security(o,n,m);
					}
			}
		else if(i==4){
			printf("ACCOUNT NOT FOUND\n");
			printf("PLEASE CONTACT XYZ BANK\n");
			return 1;
			}
		}
	}
int block(struct costomer o[],int i ,int n){
	o[i].password=000;
	printfile(o,n);
	printf("PROCESSING.......\n");
	printf("YOUR ACCOUNT IS BLOCKED \n");
	sleep(2);
	return 1;
	}
void printfile(struct costomer o[],int n){
	int i;
	FILE *p;
	p=fopen("myfile.txt","w");
	fprintf(p,"%d\n",n);
	fprintf(p,"9999\n");
	for(i=2;i<n;i++){
		fprintf(p,"%d	%d	%s	%d	%s\n",o[i].id,o[i].password,o[i].phone,o[i].totalamt,o[i].name);
		}
	fclose(p);
	}
void check(struct costomer o[],int m,int i,int n){
	printf("%d",m);
	if(m==3){
		block(o,i,n);
		printf("DUE TO MULTIPLE ATTEMPTS\nPLEASE CONTACT XYZ BANK\n");
		printf("THANKYOU");
		sleep(4);
		}
	}
void bank(){
	int i;
	time_t t;
	time(&t);
	for(i=2;i<121;i++)
		printf("#");
		printf("\t\t\t\tWELCOME TO XYZ ATM MACHINE\t\t\t\t%s",ctime(&t));
	for(i=2;i<122;i++)
		printf("#");
		printf("\t\t\t\t\t\t\t\t IF ANY PROBLEM OCCURED IN THIS MICHINE CALL:9987543264\n");
	}
