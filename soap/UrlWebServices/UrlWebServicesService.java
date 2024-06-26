
package soap.UrlWebServices;

import java.net.MalformedURLException;
import java.net.URL;
import javax.xml.namespace.QName;
import javax.xml.ws.Service;
import javax.xml.ws.WebEndpoint;
import javax.xml.ws.WebServiceClient;
import javax.xml.ws.WebServiceException;
import javax.xml.ws.WebServiceFeature;


/**
 * This class was generated by the JAX-WS RI.
 * JAX-WS RI 2.2.9-b130926.1035
 * Generated source version: 2.2
 * 
 */
@WebServiceClient(name = "UrlWebServicesService", targetNamespace = "http://soap/", wsdlLocation = "http://localhost:8888/webServ/UrlWebServices?wsdl")
public class UrlWebServicesService
    extends Service
{

    private final static URL URLWEBSERVICESSERVICE_WSDL_LOCATION;
    private final static WebServiceException URLWEBSERVICESSERVICE_EXCEPTION;
    private final static QName URLWEBSERVICESSERVICE_QNAME = new QName("http://soap/", "UrlWebServicesService");

    static {
        URL url = null;
        WebServiceException e = null;
        try {
            url = new URL("http://localhost:8888/webServ/UrlWebServices?wsdl");
        } catch (MalformedURLException ex) {
            e = new WebServiceException(ex);
        }
        URLWEBSERVICESSERVICE_WSDL_LOCATION = url;
        URLWEBSERVICESSERVICE_EXCEPTION = e;
    }

    public UrlWebServicesService() {
        super(__getWsdlLocation(), URLWEBSERVICESSERVICE_QNAME);
    }

    public UrlWebServicesService(WebServiceFeature... features) {
        super(__getWsdlLocation(), URLWEBSERVICESSERVICE_QNAME, features);
    }

    public UrlWebServicesService(URL wsdlLocation) {
        super(wsdlLocation, URLWEBSERVICESSERVICE_QNAME);
    }

    public UrlWebServicesService(URL wsdlLocation, WebServiceFeature... features) {
        super(wsdlLocation, URLWEBSERVICESSERVICE_QNAME, features);
    }

    public UrlWebServicesService(URL wsdlLocation, QName serviceName) {
        super(wsdlLocation, serviceName);
    }

    public UrlWebServicesService(URL wsdlLocation, QName serviceName, WebServiceFeature... features) {
        super(wsdlLocation, serviceName, features);
    }

    /**
     * 
     * @return
     *     returns UrlWebServices
     */
    @WebEndpoint(name = "UrlWebServicesPort")
    public UrlWebServices getUrlWebServicesPort() {
        return super.getPort(new QName("http://soap/", "UrlWebServicesPort"), UrlWebServices.class);
    }

    /**
     * 
     * @param features
     *     A list of {@link javax.xml.ws.WebServiceFeature} to configure on the proxy.  Supported features not in the <code>features</code> parameter will have their default values.
     * @return
     *     returns UrlWebServices
     */
    @WebEndpoint(name = "UrlWebServicesPort")
    public UrlWebServices getUrlWebServicesPort(WebServiceFeature... features) {
        return super.getPort(new QName("http://soap/", "UrlWebServicesPort"), UrlWebServices.class, features);
    }

    private static URL __getWsdlLocation() {
        if (URLWEBSERVICESSERVICE_EXCEPTION!= null) {
            throw URLWEBSERVICESSERVICE_EXCEPTION;
        }
        return URLWEBSERVICESSERVICE_WSDL_LOCATION;
    }

}
