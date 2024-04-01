# OpenShift

## Crear proyecto

~~~ bash
oc new-project python
oc project python
~~~

## Crear build config
~~~ bash
oc new-build --name health --binary --strategy docker
~~~

## Ejecutar build
~~~ bash
oc start-build health --from-dir .  --follow
oc logs -f bc/health
~~~


## Crear APP

~~~ bash
oc get is
oc new-app image-registry.openshift-image-registry.svc:5000/python/health
~~~

## Crear ruta

~~~ bash
oc expose service/health
oc get route

curl http://health-python.apps.shrocp4upi414ovn.lab.upshift.rdu2.redhat.com/sample/
~~~

## Agregar variables de entorno

~~~ bash
oc set env deploy/health ELAPSED_TIME_READINESS=60 ELAPSED_TIME_LIVENESS=120 ELAPSED_TIME=60
~~~