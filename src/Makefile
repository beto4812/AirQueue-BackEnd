.SUFFIXES:	.java .class

#JAVA_HOME=/usr/java/j2sdk1.4.0
#CATALINA_HOME=/home/ejfried/jakarta-tomcat-4.0.4
APPNAME=Advice
JESS=/home/alberto/diss_back/lib

SRC=$(shell find . -name '*.java' -print )
OBJ=$(SRC:.java=.class)


build: BaseServlet.class Advice.class
.java.class:
	javac \
	-classpath .:$(JAVA_HOME)/jre/lib/rt.jar:$(CATALINA_HOME)/lib/servlet-api.jar:$(JESS)/jess.jar $<
#	javac \
#	-classpath .:$(JAVA_HOME)/jre/lib/rt.jar:$(CATALINA_HOME)/lib/servlet-api.jar:$(JESS)/jess.jar BaseServlet.java


install: build
	rm -rf $(CATALINA_HOME)/webapps/$(APPNAME)/*
	mkdir -p $(CATALINA_HOME)/webapps/$(APPNAME)/WEB-INF
	cp web.xml $(CATALINA_HOME)/webapps/$(APPNAME)/WEB-INF
	mkdir -p $(CATALINA_HOME)/webapps/$(APPNAME)/WEB-INF/classes
	cp *.class *.clp $(CATALINA_HOME)/webapps/$(APPNAME)/WEB-INF/classes
	cp $(JESS)/jess.jar $(CATALINA_HOME)/lib

clean:
	rm -f *~ *.class


